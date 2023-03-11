from typing import Optional

from elasticsearch import AsyncElasticsearch

from src.core import config


es: Optional[AsyncElasticsearch] = None


async def get_elastic() -> AsyncElasticsearch:
    return es


class ESConnector:
    es: AsyncElasticsearch = None

    @classmethod
    async def setup(cls):
        cls.es = AsyncElasticsearch(
            hosts=[f"http://{config.ELASTIC_HOST}:{config.ELASTIC_PORT}"],
        )

    @classmethod
    async def close(cls):
        if cls.es:
            await cls.es.close()
            cls.es = None
