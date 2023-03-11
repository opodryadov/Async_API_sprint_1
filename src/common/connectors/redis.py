import aioredis

from src import core


class RedisConnector:
    redis: aioredis.Redis = None

    @classmethod
    async def setup(cls):
        cls.redis = await aioredis.from_url(
            url=f"redis://{core.REDIS_HOST}:{core.REDIS_PORT}",
            encoding="utf-8",
            decode_responses=True,
        )

    @classmethod
    async def close(cls):
        if cls.redis:
            await cls.redis.close()
            cls.redis = None
