import logging

from src import core
from src.common.connectors.redis import RedisConnector
from src.common.storages.base import BaseCacheStorage


logger = logging.getLogger(__name__)


class RedisStorage(BaseCacheStorage):
    def __init__(self):
        self._redis = RedisConnector()

    async def get_from_cache(self, key: str):
        data = await self._redis.redis.get(key)
        if not data:
            return None

        return data

    async def put_to_cache(self, key: str, value: str):
        await self._redis.redis.set(
            key,
            value,
            core.CACHE_EXPIRE_IN_SECONDS,
        )
