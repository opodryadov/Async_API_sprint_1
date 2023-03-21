from functools import lru_cache

from fastapi import Depends

from src.common.caches.redis_cache import RedisCacheBase
from src.common.storages.es_storage import (
    EsStorage,
    get_elastic_storage_service,
)
from src.common.storages.redis_storage import get_person_redis_storage
from src.models import Film, Person, PersonRole


class PersonService:
    def __init__(self, redis_storage: RedisCacheBase, es_storage: EsStorage):
        self._redis_storage = redis_storage
        self._es_storage = es_storage

    async def get_person_by_id(self, person_id) -> dict | None:
        person = await self._redis_storage.get_from_cache(key=person_id)
        if person:
            person = Person.parse_raw(person)
            return person.dict()

        person = await self._es_storage.get_person(person_id)
        if not person:
            return None
        person = await self._enrich_person(person)
        await self._redis_storage.put_to_cache(
            key=person.id, value=person.json()
        )

        return person.dict()

    async def get_films_by_person_id(
        self, person_id: str
    ) -> list[dict] | None:
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

    async def person_search(self, params: dict) -> list[dict] | None:
        persons = await self._get_list_persons(params)
        if not persons:
            return None
        persons = [
            person.dict()
            for person in [
                await self._enrich_person(person) for person in persons
            ]
        ]
        return persons

    async def _get_films_by_role(
        self, person_id: str, role: str
    ) -> list[Film]:
        query = dict(
            index="movies",
            body={
                "query": {
                    "nested": {
                        "path": role,
                        "query": {"match": {f"{role}.id": f"{person_id}"}},
                    }
                }
            },
        )

        key = self._redis_storage.get_key(query)
        movies = await self._redis_storage.get_from_cache(key=key)
        if movies:
            movies_deserialize = self._redis_storage.deserialize(movies)
            movies = [Film.parse_raw(movie) for movie in movies_deserialize]
            return movies

        movies = await self._es_storage.get_list_films(query)
        movies_serialize = self._redis_storage.serialize(
            [movie.json() for movie in movies]
        )
        await self._redis_storage.put_to_cache(key=key, value=movies_serialize)
        return movies

    async def _get_films_roles(self, person_id: str) -> dict:
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

    async def _enrich_person(self, person: Person) -> Person:
        films = await self._get_films_roles(person.id)
        person.films = [
            dict(uuid=key, roles=value) for key, value in films.items()
        ]
        return person

    async def _get_list_persons(self, params: dict) -> list[Person]:
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
                    "from": params.get("page_number"),
                },
            )
        else:
            query = dict(
                index="persons",
                body={"query": {"match_all": {}}},
                params={
                    "size": params.get("page_size"),
                    "from": params.get("page_number"),
                },
            )

        key = self._redis_storage.get_key(query)
        persons = await self._redis_storage.get_from_cache(key=key)
        if persons:
            persons_deserialize = self._redis_storage.deserialize(persons)
            persons = [
                Person.parse_raw(person) for person in persons_deserialize
            ]
            return persons

        persons = await self._es_storage.get_list_persons(query)
        persons_serialize = self._redis_storage.serialize(
            [person.json() for person in persons]
        )
        await self._redis_storage.put_to_cache(
            key=key, value=persons_serialize
        )
        return persons


@lru_cache()
def get_person_service(
    redis: RedisCacheBase = Depends(get_person_redis_storage),
    elastic: EsStorage = Depends(get_elastic_storage_service),
) -> PersonService:
    return PersonService(redis, elastic)
