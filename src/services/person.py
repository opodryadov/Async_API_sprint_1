from typing import Optional

from elasticsearch import NotFoundError

from src.core import config
from src.db.elastic import ESConnector
from src.db.redis import RedisConnector
from src.models import Person


class PersonService:
    def __init__(self):
        self.redis = RedisConnector()
        self.elastic = ESConnector()

    async def get_by_id(self, person_id: str) -> Optional[Person]:
        print(self.redis.__dir__())
        print(await self.redis.redis.ping())
        await self.redis.redis.set("my-key", "value")
        value = await self.redis.redis.get("my-key")
        print(value)

        person = await self._person_from_cache(person_id)
        if not person:
            person = await self._get_person_elastic(person_id)
            if not person:
                return None
            await self._put_person_to_cache(person)

        return person

    async def _get_person_elastic(self, person_id: str) -> Optional[Person]:
        try:
            doc = await self.elastic.es.get("persons", person_id)
        except NotFoundError:
            return None
        return Person(**doc["_source"])

    async def _person_from_cache(self, person_id: str) -> Optional[Person]:
        data = await self.redis.redis.get(person_id)
        if not data:
            return None

        person = Person.parse_raw(data)
        return person

    async def _put_person_to_cache(self, person: Person):
        await self.redis.redis.set(
            person.uuid, person.json(), config.CACHE_EXPIRE_IN_SECONDS
        )