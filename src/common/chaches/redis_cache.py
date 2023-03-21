import hashlib
from typing import Any

import orjson
from aioredis import Redis

from src.common.chaches.base import BaseCache
from src.common.chaches.serializer import BaseSerializer


class RedisCacheBase(BaseCache, BaseSerializer):
    cache_prefix = None
    default_ttl = 600

    def __init__(self, redis: Redis):
        self.redis = redis

    def get_key(self, *args, **kwargs):
        return hashlib.md5(
            f"{self.cache_prefix}:{self.__class__.__name__.encode('UTF-8')}:{args}:{kwargs}".encode()
        ).hexdigest()

    def serialize(self, value: list[dict[str, Any]] | list[str]) -> bytes:
        return orjson.dumps(value)

    def deserialize(self, value: str) -> list:
        return orjson.loads(value)

    async def get_from_cache(self, key: str) -> str | None:
        data = await self.redis.get(key)
        if not data:
            return None

        return data

    async def put_to_cache(self, key: str, value: bytes | str) -> None:
        await self.redis.set(
            key,
            value,
            self.default_ttl,
        )
