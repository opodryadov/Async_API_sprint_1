import pytest_asyncio
from aioresponses import aioresponses
from httpx import AsyncClient

from src.main import create_app


@pytest_asyncio.fixture(autouse=True)
def mock_aioresponse():
    with aioresponses() as m:
        yield m


@pytest_asyncio.fixture
async def test_app():
    app = create_app()
    await app.router.startup()
    try:
        yield app
    finally:
        await app.router.shutdown()


@pytest_asyncio.fixture
async def test_client(test_app):
    async with AsyncClient(app=test_app, base_url="http://test") as client:
        yield client
