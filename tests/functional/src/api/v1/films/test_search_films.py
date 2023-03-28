from http import HTTPStatus

import orjson
import pytest


pytestmark = pytest.mark.asyncio


@pytest.mark.usefixtures("flush_redis")
@pytest.mark.parametrize(
    "query, redis_key, api_response, redis_response",
    (
        (
            "nevsky",
            "86badab5aece293e7a5ad8025daff68e",
            [],
            [],
        ),
    ),
)
async def test_search_films(
    make_get_request,
    redis_client,
    query,
    redis_key,
    api_response,
    redis_response,
):
    body, status = await make_get_request(
        f"/api/v1/films/search?query={query}"
    )
    assert status == HTTPStatus.OK
    assert body == api_response

    films_in_cache = await redis_client.get(redis_key)
    if films_in_cache:
        films_deserialize = orjson.loads(films_in_cache)
        assert films_deserialize == redis_response
