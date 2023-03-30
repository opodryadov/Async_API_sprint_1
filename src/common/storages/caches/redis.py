from typing import Any

import backoff
import orjson
from redis.asyncio import (
    BusyLoadingError,
    ConnectionError,
    Redis,
    TimeoutError,
)

from src.common.handlers import backoff_handler
from src.common.storages.caches.base import BaseCache
from src.common.storages.caches.consts import DEFAULT_TTL_IN_SECONDS
from src.common.storages.caches.serializer import BaseSerializer


class RedisCacheBase(BaseCache, BaseSerializer):
    cache_prefix: str = None
    default_ttl: int = DEFAULT_TTL_IN_SECONDS

    def __init__(self, redis: Redis):
        self._redis = redis

    def get_key(self, *args, **kwargs) -> str:
        params = "::".join([str(arg) for arg in args if arg])
        return f"{self.cache_prefix}::{self.__class__.__name__}::{params}"

    def serialize(self, value: list[dict[str, Any]] | list[str]) -> bytes:
        return orjson.dumps(value)

    def deserialize(self, value: str) -> list:
        return orjson.loads(value)

    @backoff.on_exception(
        backoff.expo,
        (
            BusyLoadingError,
            ConnectionError,
            TimeoutError,
        ),
        max_tries=10,
        max_time=60,
        on_backoff=backoff_handler,
    )
    async def get_from_cache(self, key: str) -> str | None:
        data = await self._redis.get(key)
        if not data:
            return None

        return data

    @backoff.on_exception(
        backoff.expo,
        (
            BusyLoadingError,
            ConnectionError,
            TimeoutError,
        ),
        max_tries=10,
        max_time=60,
        on_backoff=backoff_handler,
    )
    async def put_to_cache(self, key: str, value: bytes | str) -> None:
        await self._redis.set(
            key,
            value,
            self.default_ttl,
        )
