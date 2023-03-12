import logging
from typing import Optional

from elasticsearch import NotFoundError

from src import core
from src.common.connectors.es import ESConnector
from src.common.connectors.redis import RedisConnector
from src.models import Person, PersonRole


logger = logging.getLogger(__name__)


class PersonService:
    def __init__(self):
        self._redis = RedisConnector()
        self._elastic = ESConnector()

    async def get_by_id(self, person_id) -> Optional[Person]:
        person = await self._person_from_cache(person_id)
        if not person:
            person = await self._get_person_elastic(person_id)
            if not person:
                return None
            await self._put_person_to_cache(person)

        return person

    async def _get_films_ids_by_actor(self, person_id: str):
        body = {
            "query": {
                "nested": {
                    "path": "actors",
                    "query": {"match": {"actors.id": f"{person_id}"}},
                }
            }
        }
        actor_movies = await self._elastic.es.search(index="movies", body=body)
        movies = {
            movie["_source"]["id"]: PersonRole.ACTOR
            for movie in actor_movies["hits"]["hits"]
        }

        return movies

    async def _get_films_ids_by_writer(self, person_id: str):
        body = {
            "query": {
                "nested": {
                    "path": "writers",
                    "query": {"match": {"writers.id": f"{person_id}"}},
                }
            }
        }
        writer_movies = await self._elastic.es.search(
            index="movies", body=body
        )
        movies = {
            movie["_source"]["id"]: PersonRole.WRITER
            for movie in writer_movies["hits"]["hits"]
        }

        return movies

    async def _get_films_ids_by_director(self, person_id: str):
        movies = None
        body = {
            "query": {
                "nested": {
                    "path": "directors",
                    "query": {"match": {"directors.id": f"{person_id}"}},
                }
            }
        }
        director_movies = await self._elastic.es.search(
            index="movies", body=body
        )
        movies = {
            movie["_source"]["id"]: PersonRole.DIRECTOR
            for movie in director_movies["hits"]["hits"]
        }

        return movies

    async def _get_films_ids_by_role(self, person_id: str):
        movies_director = await self._get_films_ids_by_director(person_id)
        movies_writer = await self._get_films_ids_by_writer(person_id)
        movies_actor = await self._get_films_ids_by_actor(person_id)

        if not movies_actor and not movies_writer and not movies_actor:
            return []
        movies = dict()

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
        films = await self._get_films_ids_by_role(person_id)
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
