import hashlib
import json
import logging
from typing import Any

import orjson

from src import core
from src.common.connectors.redis import RedisConnector
from src.common.storages.base import BaseCacheStorage


logger = logging.getLogger(__name__)


class RedisStorage(BaseCacheStorage):
    def __init__(self):
        self._redis = RedisConnector()

    @property
    def cache_prefix(self):
        return hashlib.sha1(
            self.__class__.__name__.encode("UTF-8")
        ).hexdigest()[:6]

    async def get_key(self, params: dict[str, Any]) -> str:
        return f'{self.cache_prefix}:{json.dumps({"params": params}, sort_keys=True)}'

    async def serialize(
        self, value: list[dict[str, Any]] | list[str]
    ) -> bytes:
        return orjson.dumps(value)

    async def deserialize(self, value: str) -> list:
        return orjson.loads(value)

    async def get_from_cache(self, key: str) -> str:
        data = await self._redis.redis.get(key)
        if not data:
            return None

        return data

    async def put_to_cache(self, key: str, value: bytes | str) -> None:
        await self._redis.redis.set(
            key,
            value,
            core.CACHE_EXPIRE_IN_SECONDS,
        )
