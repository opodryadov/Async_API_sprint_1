from http import HTTPStatus

import orjson
import pytest


pytestmark = pytest.mark.asyncio


@pytest.mark.usefixtures("flush_redis")
@pytest.mark.parametrize(
    "genre_id, redis_key, api_response, redis_response",
    (
        (
            "00fcd60c-e940-4362-b30a-701f428d49a4",
            "6ca8a3b2e1a505433787beb4faa893f0",
            [],
            [],
        ),
    ),
)
async def test_list_film_by_genre(
    make_get_request,
    redis_client,
    genre_id,
    redis_key,
    api_response,
    redis_response,
):
    body, status = await make_get_request(
        f"/api/v1/films?genre={genre_id}"
    )
    assert status == HTTPStatus.OK
    assert body == api_response

    films_in_cache = await redis_client.get(redis_key)
    films_deserialize = orjson.loads(films_in_cache)
    assert films_deserialize == redis_response
