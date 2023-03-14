import logging
from typing import Optional

from elasticsearch import NotFoundError

from src.common.storages.es_storage import EsStorage
from src.common.storages.redis_storage import RedisStorage
from src.models import Film, Person, PersonRole


logger = logging.getLogger(__name__)


class PersonService:
    def __init__(self):
        self._es_storage = EsStorage()
        self._redis_storage = RedisStorage()

    async def get_person_by_id(self, person_id) -> Optional[dict]:
        person = await self._redis_storage.get_from_cache(key=person_id)
        if person:
            person = Person.parse_raw(person)
            return person.dict()

        person = await self._get_person_elastic(person_id)
        if not person:
            return None
        person = await self._enrich_person(person)
        await self._redis_storage.put_to_cache(
            key=person.id, value=person.json()
        )

        return person.dict()

    async def _get_films_by_role(self, person_id: str, role: str):
        body = {
            "query": {
                "nested": {
                    "path": role,
                    "query": {"match": {f"{role}.id": f"{person_id}"}},
                }
            }
        }
        docs = await self._es_storage.search(index="movies", body=body)
        movies = [Film(**doc["_source"]) for doc in docs]
        return movies

    async def _get_films_roles(self, person_id: str):
        movies_director = {
            movie.id: PersonRole.DIRECTOR
            for movie in await self._get_films_by_role(person_id, "directors")
        }
        movies_writer = {
            movie.id: PersonRole.WRITER
            for movie in await self._get_films_by_role(person_id, "writers")
        }
        movies_actor = {
            movie.id: PersonRole.ACTOR
            for movie in await self._get_films_by_role(person_id, "actors")
        }
        movies = dict()

        if not movies_actor and not movies_writer and not movies_actor:
            return movies

        for movie in (movies_actor, movies_writer, movies_director):
            for key, value in movie.items():
                if key not in movies.keys():
                    movies[key] = [value]
                else:
                    roles = movies[key]
                    roles.append(value)
                    movies.update({key: roles})

        return movies

    async def _get_person_elastic(self, person_id: str) -> Optional[Person]:
        try:
            doc = await self._es_storage.get_by_id(
                index="persons", doc_id=person_id
            )
        except NotFoundError:
            logger.error(
                "Person was not found in ES: %s", person_id, exc_info=True
            )
            return None
        person = Person(**doc)
        return person

    async def _enrich_person(self, person: Person) -> Optional[Person]:
        films = await self._get_films_roles(person.id)
        person.films = [
            dict(uuid=key, roles=value) for key, value in films.items()
        ]
        return person

    async def get_films_by_person_id(self, person_id: str):
        films_director = await self._get_films_by_role(person_id, "directors")
        films_writer = await self._get_films_by_role(person_id, "writers")
        films_actor = await self._get_films_by_role(person_id, "actors")
        films = films_director + films_writer + films_actor
        if not films:
            return None

        films = list(
            {v["id"]: v for v in (film.dict() for film in films)}.values()
        )
        return films

    async def _get_list_genres_elastic(self, params: dict):
        if params.get("query"):
            query = dict(
                index="persons",
                body={
                    "query": {
                        "multi_match": {
                            "query": params.get("query"),
                            "fields": ["full_name"],
                            "type": "phrase_prefix",
                            "tie_breaker": 0.3,
                        }
                    }
                },
                params={
                    "size": params.get("page_size"),
                    "from": params.get("page_number") - 1,
                },
            )
        else:
            query = dict(
                index="persons",
                body={"query": {"match_all": {}}},
                params={
                    "size": params.get("page_size"),
                    "from": params.get("page_number") - 1,
                },
            )
        docs = await self._es_storage.search(**query)
        return [Person(**doc["_source"]) for doc in docs]

    async def person_search(self, params: dict):
        persons = await self._get_list_genres_elastic(params)
        if not persons:
            return None
        persons = [
            person.dict()
            for person in [
                await self._enrich_person(person) for person in persons
            ]
        ]
        return persons
