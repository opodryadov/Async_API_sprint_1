from typing import Optional

import backoff
from redis.asyncio import (
    BusyLoadingError,
    ConnectionError,
    Redis,
    TimeoutError,
)

from src.common.handlers import backoff_handler


redis: Optional[Redis] = None


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
async def get_redis() -> Redis:
    return redis
