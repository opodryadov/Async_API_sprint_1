from typing import Optional

import aioredis
from aioredis import Redis

from src.core import config


redis: Optional[Redis] = None


async def get_redis() -> Redis:
    return redis


class RedisConnector:
    redis: Redis = None

    @classmethod
    async def setup(cls):
        cls.redis = await aioredis.from_url(
            url=f"redis://{config.REDIS_HOST}:{config.REDIS_PORT}",
            encoding="utf-8",
            decode_responses=True,
        )

    @classmethod
    async def close(cls):
        if cls.redis:
            await cls.redis.close()
            cls.redis = None
