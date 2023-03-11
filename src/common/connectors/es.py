from elasticsearch import AsyncElasticsearch

from src.core import config


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
