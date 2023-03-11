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

    async def get_by_id(self, query: dict) -> Optional[Person]:
        person_id: str = query.get("person_id")
        person = await self._person_from_cache(person_id)
        if not person:
            body = {
                "query": {
                    "nested": {
                        "path": "actors",
                        "query": {"match": {"actors.id": f"{person_id}"}},
                    }
                }
            }
            person_role_actors_movies = await self._elastic.es.search(
                index="movies", body=body
            )
            movies = [
                movie["_source"]
                for movie in person_role_actors_movies["hits"]["hits"]
            ]
            person = await self._get_person_elastic(person_id)
            person.role = "actor"
            person.film_ids = [movie.get("id") for movie in movies]
            if not person:
                return None
            await self._put_person_to_cache(person)

        return person

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
