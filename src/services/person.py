import logging
from typing import Optional

from elasticsearch import NotFoundError

from src import core
from src.common.connectors.es import ESConnector
from src.common.connectors.redis import RedisConnector
from src.models import Film, Person, PersonRole


logger = logging.getLogger(__name__)


class PersonService:
    def __init__(self):
        self._redis = RedisConnector()
        self._elastic = ESConnector()

    async def get_person_by_id(self, person_id) -> Optional[dict]:
        person = await self._person_from_cache(person_id)
        if not person:
            person = await self._get_person_elastic(person_id)
            if not person:
                return None
            person = await self._enrich_person(person)
            await self._put_person_to_cache(person)

        return person.dict()

    async def _get_films_by_actor(self, person_id: str):
        body = {
            "query": {
                "nested": {
                    "path": "actors",
                    "query": {"match": {"actors.id": f"{person_id}"}},
                }
            }
        }
        docs = await self._elastic.es.search(index="movies", body=body)
        movies = [Film(**doc["_source"]) for doc in docs["hits"]["hits"]]

        return movies

    async def _get_films_by_writer(self, person_id: str):
        body = {
            "query": {
                "nested": {
                    "path": "writers",
                    "query": {"match": {"writers.id": f"{person_id}"}},
                }
            }
        }
        docs = await self._elastic.es.search(index="movies", body=body)
        movies = [Film(**doc["_source"]) for doc in docs["hits"]["hits"]]

        return movies

    async def _get_films_by_director(self, person_id: str):
        body = {
            "query": {
                "nested": {
                    "path": "directors",
                    "query": {"match": {"directors.id": f"{person_id}"}},
                }
            }
        }
        docs = await self._elastic.es.search(index="movies", body=body)
        movies = [Film(**doc["_source"]) for doc in docs["hits"]["hits"]]

        return movies

    async def _get_films_roles(self, person_id: str):
        movies_director = {
            movie.id: PersonRole.DIRECTOR
            for movie in await self._get_films_by_director(person_id)
        }
        movies_writer = {
            movie.id: PersonRole.WRITER
            for movie in await self._get_films_by_writer(person_id)
        }
        movies_actor = {
            movie.id: PersonRole.ACTOR
            for movie in await self._get_films_by_actor(person_id)
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
            doc = await self._elastic.es.get(index="persons", id=person_id)
        except NotFoundError:
            logger.error(
                "Person was not found in ES: %s", person_id, exc_info=True
            )
            return None
        person = Person(**doc["_source"])
        return person

    async def _enrich_person(self, person: Person) -> Optional[Person]:
        films = await self._get_films_roles(person.id)
        person.films = [
            dict(uuid=key, roles=value) for key, value in films.items()
        ]
        return person

    async def _person_from_cache(self, person_id: str) -> Optional[Person]:
        data = await self._redis.redis.get(person_id)
        if not data:
            return None

        person = Person.parse_raw(data)
        return person

    async def _put_person_to_cache(self, person: Person):
        await self._redis.redis.set(
            person.id,
            person.json(),
            core.CACHE_EXPIRE_IN_SECONDS,
        )

    async def get_films_by_person_id(self, person_id: str):
        # Прридумать как сохранить в кэше
        films_director = await self._get_films_by_director(person_id)
        films_writer = await self._get_films_by_writer(person_id)
        films_actor = await self._get_films_by_actor(person_id)
        films = films_director + films_writer + films_actor
        if not films:
            return None

        films = list(
            {v["id"]: v for v in (film.dict() for film in films)}.values()
        )
        return films

    async def _get_list_genres_elastic(
        self, query: str, page_size: int, page_number: int
    ):
        if query:
            params = dict(
                index="persons",
                body={
                    "query": {
                        "match": {
                            "full_name": {
                                "query": query,
                                "fuzziness": 1,
                                "operator": "or",
                            }
                        }
                    }
                },
                params={
                    "size": page_size,
                    "from": page_number,
                },
            )
        else:
            params = dict(
                index="persons",
                body={"query": {"match_all": {}}},
                params={
                    "size": page_size,
                    "from": page_number,
                },
            )
        docs = await self._elastic.es.search(**params)
        return [Person(**doc["_source"]) for doc in docs["hits"]["hits"]]

    async def person_search(
        self, query: str, page_size: int, page_number: int
    ):
        persons = await self._get_list_genres_elastic(
            query, page_size, page_number
        )
        if not persons:
            return None
        persons = [
            person.dict()
            for person in [
                await self._enrich_person(person) for person in persons
            ]
        ]
        return persons
