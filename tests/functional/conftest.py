import json

import aioredis
import pytest
from elasticsearch import AsyncElasticsearch
from elasticsearch.helpers import async_bulk
from httpx import AsyncClient

from tests.functional.core import test_settings
from tests.functional.testdata.consts import INDEXES


@pytest.fixture
async def test_app():
    from src.main import app

    await app.router.startup()
    try:
        yield app
    finally:
        await app.router.shutdown()


@pytest.fixture
async def test_client(test_app):
    url = f"http://{test_settings.project_host}:{test_settings.project_port}/api/v1"
    async with AsyncClient(app=test_app, base_url=url) as client:
        yield client


@pytest.fixture(scope="session")
async def redis_client():
    async with aioredis.from_url(
        url=f"redis://{test_settings.redis_host}:{test_settings.redis_port}",
        encoding="utf-8",
        decode_responses=True,
    ) as pool:
        yield pool


@pytest.fixture(scope="session", autouse=True)
async def es_client():
    async with AsyncElasticsearch(
        hosts=f"http://{test_settings.elastic_host}:{test_settings.elastic_port}",
        use_ssl=False,
        verify_certs=False,
    ) as pool:
        yield pool


# @pytest.fixture
# async def flush_redis(redis_client):
#     yield
#     await redis_client.flushdb()
#
#
# @pytest.fixture
# async def flush_indexes(es_client):
#     for index in INDEXES:
#         await es_client.indices.delete(index=index.index_name)


@pytest.fixture(scope="session", autouse=True)
async def es_init(es_client: AsyncElasticsearch):
    for index in INDEXES:
        if not await es_client.indices.exists(index=index.index_name):
            json_data = json.loads(open(index.schema_file_path).read())
            await es_client.indices.create(
                index=index.index_name, body=json_data
            )

        items = json.loads(open(index.data_file_path).read())
        processed, errors = await async_bulk(
            client=es_client, actions=items, chunk_size=100
        )
        if errors:
            print("Migration failed: %s", errors)
        print("Migration: processed %s errors %s", processed, errors)
