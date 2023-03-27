from http import HTTPStatus

import orjson
import pytest

from tests.functional.testdata.vars.films import (
    SEARCH_FILMS_SORT_BY_RATING_ASC_RESPONSE,
    SEARCH_FILMS_SORT_BY_RATING_ASC_IN_CACHE,
    SEARCH_FILMS_SORT_BY_TITLE_ASC_RESPONSE,
    SEARCH_FILMS_SORT_BY_TITLE_ASC_IN_CACHE,
    SEARCH_FILMS_SORT_BY_RATING_DESC_RESPONSE,
    SEARCH_FILMS_SORT_BY_RATING_DESC_IN_CACHE,
    SEARCH_FILMS_SORT_BY_TITLE_DESC_RESPONSE,
    SEARCH_FILMS_SORT_BY_TITLE_DESC_IN_CACHE,
)


pytestmark = pytest.mark.asyncio


@pytest.mark.usefixtures("flush_redis")
@pytest.mark.parametrize(
    "query, sort, redis_key, api_response, redis_response",
    (
        (
            "luxury",
            "imdb_rating",
            "3b465990a7b0af63cdbaae3be7937c60",
            SEARCH_FILMS_SORT_BY_RATING_ASC_RESPONSE,
            SEARCH_FILMS_SORT_BY_RATING_ASC_IN_CACHE,
        ),
        (
            "luxury",
            "title",
            "1be737ce1275cb7f88d911b858896fdb",
            SEARCH_FILMS_SORT_BY_TITLE_ASC_RESPONSE,
            SEARCH_FILMS_SORT_BY_TITLE_ASC_IN_CACHE,
        ),
        (
            "luxury",
            "-imdb_rating",
            "a730349861e98b7652aadaaa47fb6d12",
            SEARCH_FILMS_SORT_BY_RATING_DESC_RESPONSE,
            SEARCH_FILMS_SORT_BY_RATING_DESC_IN_CACHE,
        ),
        (
            "luxury",
            "-title",
            "0ba189f091d383f11522147cb3a1b4ba",
            SEARCH_FILMS_SORT_BY_TITLE_DESC_RESPONSE,
            SEARCH_FILMS_SORT_BY_TITLE_DESC_IN_CACHE,
        ),
        (
            "nevsky",
            None,
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
    sort,
    redis_key,
    api_response,
    redis_response,
):
    body, status = await make_get_request(
        f"/api/v1/films/search?query={query}&sort={sort}"
    )
    assert status == HTTPStatus.OK
    assert body == api_response

    films_in_cache = await redis_client.get(redis_key)
    if films_in_cache:
        films_deserialize = orjson.loads(films_in_cache)
        assert films_deserialize == redis_response
