from typing import Optional

import backoff
from elasticsearch import (
    AsyncElasticsearch,
    ConnectionError,
    ConnectionTimeout,
)

from src.common.handlers import backoff_handler


es: Optional[AsyncElasticsearch] = None


@backoff.on_exception(
    backoff.expo,
    (
        ConnectionError,
        ConnectionTimeout,
    ),
    max_tries=10,
    max_time=60,
    on_backoff=backoff_handler,
)
async def get_elastic() -> AsyncElasticsearch:
    return es
