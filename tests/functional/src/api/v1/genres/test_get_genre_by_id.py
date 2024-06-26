from http import HTTPStatus

import orjson
import pytest

from tests.functional.testdata.vars.genres import CACHE_GENRE_NAME, GENRE_NAME


pytestmark = pytest.mark.asyncio


@pytest.mark.usefixtures("flush_redis")
async def test_get_genre_by_id(make_get_request, redis_client):
    genre_id = "0b105f87-e0a5-45dc-8ce7-f8632088f390"

    body, status = await make_get_request(f"/api/v1/genres/{genre_id}")
    assert status == HTTPStatus.OK
    assert body == GENRE_NAME

    genre_in_cache = await redis_client.get(genre_id)
    genre_deserialize = orjson.loads(genre_in_cache)
    assert genre_deserialize == CACHE_GENRE_NAME


async def test_get_genre_not_found(make_get_request, redis_client):
    genre_id = "9296b07c-5c26-4637-a662-8b6c91bb769b"

    body, status = await make_get_request(f"/api/v1/genres/{genre_id}")
    assert status == HTTPStatus.NOT_FOUND
    assert body == {"detail": "Genre not found"}

    genre_in_cache = await redis_client.get(genre_id)
    assert genre_in_cache is None
