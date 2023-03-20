import asyncio
import json
from typing import AsyncIterable

import pytest
import pytest_asyncio
import redis
from aioresponses import aioresponses
from elasticsearch import AsyncElasticsearch
from elasticsearch.helpers import async_bulk
from httpx import AsyncClient

from tests.functional.core import test_settings
from tests.functional.testdata.consts import INDEXES


@pytest.fixture(scope="session")
def event_loop(request: "pytest.FixtureRequest"):
    """Переопределение фикстуры из pytest-asyncio, чтобы можно было создавать асинхронные фикстуры со scope=session"""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(autouse=True)
def mock_aioresponse():
    with aioresponses() as m:
        yield m


@pytest_asyncio.fixture
async def test_app():
    from src.main import app

    await app.router.startup()
    try:
        yield app
    finally:
        await app.router.shutdown()


@pytest_asyncio.fixture
async def test_client(test_app) -> AsyncIterable[AsyncClient]:
    url = f"http://{test_settings.project_host}:{test_settings.project_port}"
    async with AsyncClient(app=test_app, base_url=url) as client:
        yield client


@pytest.fixture(scope="session")
def redis_client():
    # async with aioredis.from_url(
    #     url=f"redis://{test_settings.redis_host}:{test_settings.redis_port}",
    #     encoding="utf-8",
    #     decode_responses=True,
    # ) as pool:
    #     yield pool
    return redis.Redis(test_settings.redis_host, test_settings.redis_port)


@pytest_asyncio.fixture(scope="session")
async def es_client():
    pool = AsyncElasticsearch(
        hosts=f"http://{test_settings.elastic_host}:{test_settings.elastic_port}"
    )
    yield pool
    await pool.close()


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


@pytest_asyncio.fixture(scope="session", autouse=True)
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
