import hashlib
import json
import logging
from functools import lru_cache
from typing import Any

import orjson
from aioredis import Redis
from fastapi import Depends

from src.common.db.redis import get_redis
from src.common.storages.base import BaseCacheStorage
from src.core import settings


logger = logging.getLogger(__name__)


class RedisStorage(BaseCacheStorage):
    def __init__(self, redis: Redis):
        self._redis = redis

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

    async def get_from_cache(self, key: str) -> str | None:
        data = await self._redis.get(key)
        if not data:
            return None

        return data

    async def put_to_cache(self, key: str, value: bytes | str) -> None:
        await self._redis.set(
            key,
            value,
            settings.cache_expire,
        )


@lru_cache()
def get_redis_storage_service(
    redis: Redis = Depends(get_redis),
) -> RedisStorage:
    return RedisStorage(redis)
