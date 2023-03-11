from elasticsearch import AsyncElasticsearch

from src import core


class ESConnector:
    es: AsyncElasticsearch = None

    @classmethod
    async def setup(cls):
        cls.es = AsyncElasticsearch(
            hosts=[f"http://{core.ELASTIC_HOST}:{core.ELASTIC_PORT}"],
        )

    @classmethod
    async def close(cls):
        if cls.es:
            await cls.es.close()
            cls.es = None
