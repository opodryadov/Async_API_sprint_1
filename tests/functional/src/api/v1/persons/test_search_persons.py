from http import HTTPStatus

import orjson
import pytest

from tests.functional.testdata.vars.persons import (
    SEARCH_FILMS_IN_CACHE,
    SEARCH_FILMS_RESPONSE,
)


pytestmark = pytest.mark.asyncio


@pytest.mark.usefixtures("flush_redis")
@pytest.mark.parametrize(
    "query, redis_key, api_response, cache_response",
    (
        (
            "pine",
            "384f7626fe81126324e3395d25f385d9",
            SEARCH_FILMS_RESPONSE,
            SEARCH_FILMS_IN_CACHE,
        ),
        (
            "test",
            "b0ddc099e188de1b27236cd50e14f65a",
            [],
            [],
        ),
    ),
)
async def test_search_persons(
    make_get_request,
    redis_client,
    query,
    api_response,
    redis_key,
    cache_response,
):
    body, status = await make_get_request(
        f"/api/v1/persons/search?query={query}"
    )
    assert status == HTTPStatus.OK
    assert body == api_response

    record_in_cache = await redis_client.get(redis_key)
    if record_in_cache:
        record_deserealize = orjson.loads(record_in_cache)
        assert record_deserealize == cache_response
