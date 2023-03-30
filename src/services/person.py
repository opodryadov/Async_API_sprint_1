from functools import lru_cache

from fastapi import Depends

from src.common.storages.caches.redis import RedisCacheBase
from src.models import Film, Person, PersonRole
from src.models.search import IndexName
from src.services.base import Service
from src.services.es_storage import PersonEsStorage, get_person_elastic_storage
from src.services.redis_storage import (
    PersonRedisStorage,
    get_person_redis_storage,
)


class PersonService(Service):
    index_name = IndexName.PERSONS.value
    detail_model = Person
    model = Person

    def __init__(
        self, redis_storage: RedisCacheBase, es_storage: PersonEsStorage
    ):
        super().__init__(redis_storage, es_storage)
        self._redis_storage = redis_storage
        self._es_storage = es_storage

    async def get_person_by_id(self, person_id) -> dict | None:
        person = await self.get_by_id(person_id)
        if not person:
            return
        person = await self._enrich_person(person)
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
        persons = await self.get_list(params)
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
        key = self._redis_storage.get_key(person_id, role)
        movies = await self._redis_storage.get_from_cache(key=key)
        if movies:
            movies_deserialize = self._redis_storage.deserialize(movies)
            movies = [Film.parse_raw(movie) for movie in movies_deserialize]
            return movies

        movies = await self._es_storage.get_films_by_role(person_id, role)
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


@lru_cache()
def get_person_service(
    redis: PersonRedisStorage = Depends(get_person_redis_storage),
    elastic: PersonEsStorage = Depends(get_person_elastic_storage),
) -> PersonService:
    return PersonService(redis, elastic)
