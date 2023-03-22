from typing import Optional

import backoff
from aioredis import Redis, ConnectionError


redis: Optional[Redis] = None


@backoff.on_exception(
    backoff.expo,
    (ConnectionError,),
    max_tries=10,
)
async def get_redis() -> Redis:
    return redis
