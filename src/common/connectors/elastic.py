from typing import Optional

import backoff
from elasticsearch import AsyncElasticsearch, ConnectionError


es: Optional[AsyncElasticsearch] = None


@backoff.on_exception(
    backoff.expo,
    (ConnectionError,),
    max_tries=10,
)
async def get_elastic() -> AsyncElasticsearch:
    return es
