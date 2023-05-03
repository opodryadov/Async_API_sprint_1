import asyncio
import json
import logging
import re
from http import HTTPStatus

import aiohttp
import pytest
import respx
from elasticsearch import AsyncElasticsearch
from elasticsearch.helpers import async_bulk
from httpx import AsyncClient
from redis import asyncio as aioredis

from tests.functional.core import test_settings
from tests.functional.src.api.v1.roles.test_get_roles import (
    GET_ALL_ROLES_RESPONSE,
)
from tests.functional.testdata.consts import INDEXES


logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def session(event_loop):
    session = aiohttp.ClientSession(trust_env=False)
    yield session
    await session.close()


@pytest.fixture
def make_get_request(session):
    async def inner(method: str, params: dict = None):
        params = params or {}
        url = (
            f"http://{test_settings.project_host}:{test_settings.project_port}"
            + method
        )
        async with session.get(url, params=params) as response:
            body = await response.json()
            status = response.status
            return body, status

    return inner


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


@pytest.fixture
async def flush_redis(redis_client):
    await redis_client.flushdb()


async def flush_indexes(es_client: AsyncElasticsearch):
    for index in INDEXES:
        await es_client.indices.delete(index=index.index_name)


async def write_test_data(es_client: AsyncElasticsearch):
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
            logger.error("Migration failed: %s", errors)
        logger.info("Migration: processed %s errors %s", processed, errors)


@pytest.fixture(scope="session", autouse=True)
async def es_init(es_client: AsyncElasticsearch):
    await write_test_data(es_client)

    yield

    await flush_indexes(es_client)


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
    async with AsyncClient(app=test_app, base_url="http://test") as client:
        yield client


@pytest.fixture
def mock_external_services():
    with respx.mock(base_url="http://0.0.0.0/") as respx_mock:
        yield respx_mock


@pytest.fixture
async def mock_auth_api_ok(mock_external_services):
    mock_external_services.get(re.compile(".*/api/srv/roles")).respond(
        json=GET_ALL_ROLES_RESPONSE,
        status_code=HTTPStatus.OK,
    )
