from http import HTTPStatus

import orjson
import pytest

from tests.functional.testdata.vars.films import (
    GENRE_FILMS_SORT_BY_TITLE_ASC_RESPONSE,
    GENRE_FILMS_SORT_BY_TITLE_ASC_IN_CACHE,
    GENRE_FILMS_SORT_BY_RATING_ASC_RESPONSE,
    GENRE_FILMS_SORT_BY_RATING_ASC_IN_CACHE,
    GENRE_FILMS_SORT_BY_TITLE_DESC_RESPONSE,
    GENRE_FILMS_SORT_BY_TITLE_DESC_IN_CACHE,
    GENRE_FILMS_SORT_BY_RATING_DESC_RESPONSE,
    GENRE_FILMS_SORT_BY_RATING_DESC_IN_CACHE,
)


pytestmark = pytest.mark.asyncio


@pytest.mark.usefixtures("flush_redis")
@pytest.mark.parametrize(
    "genre_id, sort, redis_key, api_response, redis_response",
    (
        (
            "5373d043-3f41-4ea8-9947-4b746c601bbd",
            "title",
            "08dab16fecd973c507ecb2bde4f21b4c",
            GENRE_FILMS_SORT_BY_TITLE_ASC_RESPONSE,
            GENRE_FILMS_SORT_BY_TITLE_ASC_IN_CACHE,
        ),
        (
            "31cabbb5-6389-45c6-9b48-f7f173f6c40f",
            "imdb_rating",
            "86b4d7f80994b6bf56ed8fa4a09dd17d",
            GENRE_FILMS_SORT_BY_RATING_ASC_RESPONSE,
            GENRE_FILMS_SORT_BY_RATING_ASC_IN_CACHE,
        ),
        (
            "55c723c1-6d90-4a04-a44b-e9792040251a",
            "-title",
            "b84906f77de129d4ef369124d8b3ef81",
            GENRE_FILMS_SORT_BY_TITLE_DESC_RESPONSE,
            GENRE_FILMS_SORT_BY_TITLE_DESC_IN_CACHE,
        ),
        (
            "f39d7b6d-aef2-40b1-aaf0-cf05e7048011",
            "-imdb_rating",
            "43e74e1bbeeec1d3e52ad1b3d1593e20",
            GENRE_FILMS_SORT_BY_RATING_DESC_RESPONSE,
            GENRE_FILMS_SORT_BY_RATING_DESC_IN_CACHE,
        ),
        (
            "00fcd60c-e940-4362-b30a-701f428d49a4",
            None,
            "6ca8a3b2e1a505433787beb4faa893f0",
            [],
            [],
        )
    ),
)
async def test_list_film_by_genre(
    make_get_request,
    redis_client,
    genre_id,
    sort,
    redis_key,
    api_response,
    redis_response,
):
    body, status = await make_get_request(
        f"/api/v1/films?genre={genre_id}&sort={sort}"
    )
    assert status == HTTPStatus.OK
    assert body == api_response

    films_in_cache = await redis_client.get(redis_key)
    films_deserialize = orjson.loads(films_in_cache)
    assert films_deserialize == redis_response
