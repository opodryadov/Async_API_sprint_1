from http import HTTPStatus

import orjson
import pytest

from tests.functional.testdata.vars.genres import (
    ALL_GENRES,
    CACHE_ALL_GENRES,
)


pytestmark = pytest.mark.asyncio


@pytest.mark.usefixtures("flush_redis")
async def test_get_all_genres(make_get_request, redis_client):
    redis_key = "bff0b4bf49e1bf3ff01d8b1fc8a11ca1"

    body, status = await make_get_request("/api/v1/genres")
    assert status == HTTPStatus.OK
    assert body == ALL_GENRES

    genres_in_cache = await redis_client.get(redis_key)
    genres_deserialize = orjson.loads(genres_in_cache)
    assert genres_deserialize == CACHE_ALL_GENRES
