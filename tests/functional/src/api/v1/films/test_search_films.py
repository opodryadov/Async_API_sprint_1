from http import HTTPStatus

import orjson
import pytest

from tests.functional.testdata.vars.films import (
    SEARCH_FILM_QUERY_TITLE_RESPONSE,
    SEARCH_FILM_QUERY_TITLE_IN_CACHE,
    SEARCH_FILM_QUERY_DESCRIPTION_RESPONSE,
    SEARCH_FILM_QUERY_DESCRIPTION_IN_CACHE,
    SEARCH_FILMS_WITHOUT_QUERY_RESPONSE,
    SEARCH_FILMS_WITHOUT_QUERY_IN_CACHE,
)


pytestmark = pytest.mark.asyncio


@pytest.mark.usefixtures("flush_redis")
@pytest.mark.parametrize(
    "query, redis_key, api_response, redis_response",
    (
        (
            "star",
            "1cacf91f2391fba91b03cc85ac913393",
            SEARCH_FILM_QUERY_TITLE_RESPONSE,
            SEARCH_FILM_QUERY_TITLE_IN_CACHE,
        ),
        (
            "luxury",
            "0bbe14abf2a3eaf6ecd9152a8d4f661c",
            SEARCH_FILM_QUERY_DESCRIPTION_RESPONSE,
            SEARCH_FILM_QUERY_DESCRIPTION_IN_CACHE,
        ),
        (
            "nevsky",
            "86badab5aece293e7a5ad8025daff68e",
            [],
            [],
        ),
        (
            "",
            "fdee7c6a87511871e7c6fb9234fa0220",
            SEARCH_FILMS_WITHOUT_QUERY_RESPONSE,
            SEARCH_FILMS_WITHOUT_QUERY_IN_CACHE,
        ),
    ),
)
async def test_search_films(
    make_get_request,
    redis_client,
    es_client,
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

    if body:
        for i in range(0, -2, -1):
            documents = await es_client.get(index="movies", id=body[i]["uuid"])
            film_title = documents["_source"]["title"]
            film_description = documents["_source"]["description"]
            assert query[:3].lower() in film_title.lower() \
                   or query[:3].lower() in film_description.lower()

    films_in_cache = await redis_client.get(redis_key)
    if films_in_cache:
        films_deserialize = orjson.loads(films_in_cache)
        assert films_deserialize == redis_response
