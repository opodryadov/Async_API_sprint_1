from elasticsearch import AsyncElasticsearch

from src.core import settings


class ESConnector:
    es: AsyncElasticsearch = None

    @classmethod
    async def setup(cls):
        cls.es = AsyncElasticsearch(
            hosts=[f"http://{settings.elastic_host}:{settings.elastic_port}"],
        )

    @classmethod
    async def close(cls):
        if cls.es:
            await cls.es.close()
            cls.es = None
