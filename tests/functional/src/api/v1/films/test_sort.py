from http import HTTPStatus

import orjson
import pytest

from tests.functional.testdata.vars.sort import (
    SORT_FILMS_BY_TITLE_ASC_RESPONSE,
    SORT_FILMS_BY_TITLE_ASC_IN_CACHE,
    SORT_FILMS_BY_TITLE_DESC_RESPONSE,
    SORT_FILMS_BY_TITLE_DESC_IN_CACHE,
    SORT_FILMS_BY_RATING_ASC_RESPONSE,
    SORT_FILMS_BY_RATING_ASC_IN_CACHE,
    SORT_FILMS_BY_RATING_DESC_RESPONSE,
    SORT_FILMS_BY_RATING_DESC_IN_CACHE,
    FILMS_WITHOUT_SORT_RESPONSE,
    FILMS_WITHOUT_SORT_IN_CACHE,
)


pytestmark = pytest.mark.asyncio


@pytest.mark.usefixtures("flush_redis")
@pytest.mark.parametrize(
    "endpoint",
    ("films", "films/search",),
)
@pytest.mark.parametrize(
    "sort, redis_key, api_response, redis_response",
    (
        (
            "title",
            "56c16686d7db7a898a4497ac4bb1f606",
            SORT_FILMS_BY_TITLE_ASC_RESPONSE,
            SORT_FILMS_BY_TITLE_ASC_IN_CACHE,
        ),
        (
            "-title",
            "cd031934148e379c4eeff19f1c6c82c3",
            SORT_FILMS_BY_TITLE_DESC_RESPONSE,
            SORT_FILMS_BY_TITLE_DESC_IN_CACHE,
        ),
        (
            "imdb_rating",
            "d0ce600b4fca81245149cd6186bce635",
            SORT_FILMS_BY_RATING_ASC_RESPONSE,
            SORT_FILMS_BY_RATING_ASC_IN_CACHE,
        ),
        (
            "-imdb_rating",
            "177f0c498b841313677b79bd9ec1f013",
            SORT_FILMS_BY_RATING_DESC_RESPONSE,
            SORT_FILMS_BY_RATING_DESC_IN_CACHE,
        ),
        (
            "",
            "fdee7c6a87511871e7c6fb9234fa0220",
            FILMS_WITHOUT_SORT_RESPONSE,
            FILMS_WITHOUT_SORT_IN_CACHE,
        ),
        (
            "unknown",
            "fdee7c6a87511871e7c6fb9234fa0220",
            FILMS_WITHOUT_SORT_RESPONSE,
            FILMS_WITHOUT_SORT_IN_CACHE,
        ),
    ),
)
async def test_sort_list_films(
    make_get_request,
    redis_client,
    endpoint,
    sort,
    redis_key,
    api_response,
    redis_response,
):
    body, status = await make_get_request(
        f"/api/v1/{endpoint}?sort={sort}"
    )
    assert status == HTTPStatus.OK
    assert body == api_response

    films_in_cache = await redis_client.get(redis_key)
    films_deserialize = orjson.loads(films_in_cache)
    assert films_deserialize == redis_response
