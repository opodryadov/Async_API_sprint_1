import logging
from typing import Optional

from elasticsearch import NotFoundError

from src import core
from src.common.connectors.es import ESConnector
from src.common.connectors.redis import RedisConnector
from src.models import Person


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
        movies_ids = [
            movie["_source"]["id"] for movie in actor_movies["hits"]["hits"]
        ]
        return movies_ids

    async def _get_person_elastic(self, person_id: str) -> Optional[Person]:
        try:
            doc = await self._elastic.es.get(index="persons", id=person_id)
        except NotFoundError:
            logger.error(
                "Person was not found in ES: %s", person_id, exc_info=True
            )
            return None
        person = Person(**doc["_source"])
        person.role = "actor"
        person.film_ids = await self._get_films_ids_by_actor(person_id)
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
            person.json(by_alias=True),
            core.CACHE_EXPIRE_IN_SECONDS,
        )
