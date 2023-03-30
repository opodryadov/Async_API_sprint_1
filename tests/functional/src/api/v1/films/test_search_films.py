from http import HTTPStatus

import orjson
import pytest

from tests.functional.testdata.vars.films import (
    SEARCH_FILM_QUERY_DESCRIPTION_IN_CACHE,
    SEARCH_FILM_QUERY_DESCRIPTION_RESPONSE,
    SEARCH_FILM_QUERY_TITLE_IN_CACHE,
    SEARCH_FILM_QUERY_TITLE_RESPONSE,
    SEARCH_FILMS_WITHOUT_QUERY_IN_CACHE,
    SEARCH_FILMS_WITHOUT_QUERY_RESPONSE,
)
from tests.functional.testdata.vars.sort import (
    FILMS_WITHOUT_SORT_IN_CACHE,
    FILMS_WITHOUT_SORT_RESPONSE,
    SORT_FILMS_BY_RATING_ASC_IN_CACHE,
    SORT_FILMS_BY_RATING_ASC_RESPONSE,
    SORT_FILMS_BY_RATING_DESC_IN_CACHE,
    SORT_FILMS_BY_RATING_DESC_RESPONSE,
    SORT_FILMS_BY_TITLE_ASC_IN_CACHE,
    SORT_FILMS_BY_TITLE_ASC_RESPONSE,
    SORT_FILMS_BY_TITLE_DESC_IN_CACHE,
    SORT_FILMS_BY_TITLE_DESC_RESPONSE,
)


pytestmark = pytest.mark.asyncio


@pytest.mark.usefixtures("flush_redis")
@pytest.mark.parametrize(
    "query, redis_key, api_response, redis_response",
    (
        (
            "star",
            "movies::FilmRedisStorage::star::{}::1::50::search_films",
            SEARCH_FILM_QUERY_TITLE_RESPONSE,
            SEARCH_FILM_QUERY_TITLE_IN_CACHE,
        ),
        (
            "luxury",
            "movies::FilmRedisStorage::luxury::{}::1::50::search_films",
            SEARCH_FILM_QUERY_DESCRIPTION_RESPONSE,
            SEARCH_FILM_QUERY_DESCRIPTION_IN_CACHE,
        ),
        (
            "nevsky",
            "movies::FilmRedisStorage::nevsky::{}::1::50::search_films",
            [],
            [],
        ),
        (
            "",
            "movies::FilmRedisStorage::::{}::1::50::search_films",
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
            assert (
                query[:3].lower() in film_title.lower()
                or query[:3].lower() in film_description.lower()
            )

    films_in_cache = await redis_client.get(redis_key)
    if films_in_cache:
        films_deserialize = orjson.loads(films_in_cache)
        assert films_deserialize == redis_response


@pytest.mark.usefixtures("flush_redis")
@pytest.mark.parametrize(
    "sort, redis_key, api_response, redis_response",
    (
        (
            "title",
            "movies::FilmRedisStorage::{'title.raw': 'asc'}::1::50::search_films",
            SORT_FILMS_BY_TITLE_ASC_RESPONSE,
            SORT_FILMS_BY_TITLE_ASC_IN_CACHE,
        ),
        (
            "-title",
            "movies::FilmRedisStorage::{'title.raw': 'desc'}::1::50::search_films",
            SORT_FILMS_BY_TITLE_DESC_RESPONSE,
            SORT_FILMS_BY_TITLE_DESC_IN_CACHE,
        ),
        (
            "imdb_rating",
            "movies::FilmRedisStorage::{'imdb_rating': 'asc'}::1::50::search_films",
            SORT_FILMS_BY_RATING_ASC_RESPONSE,
            SORT_FILMS_BY_RATING_ASC_IN_CACHE,
        ),
        (
            "-imdb_rating",
            "movies::FilmRedisStorage::{'imdb_rating': 'desc'}::1::50::search_films",
            SORT_FILMS_BY_RATING_DESC_RESPONSE,
            SORT_FILMS_BY_RATING_DESC_IN_CACHE,
        ),
        (
            "",
            "movies::FilmRedisStorage::1::50::search_films",
            FILMS_WITHOUT_SORT_RESPONSE,
            FILMS_WITHOUT_SORT_IN_CACHE,
        ),
        (
            "unknown",
            "movies::FilmRedisStorage::1::50::search_films",
            FILMS_WITHOUT_SORT_RESPONSE,
            FILMS_WITHOUT_SORT_IN_CACHE,
        ),
    ),
)
async def test_sort_list_films(
    make_get_request,
    redis_client,
    sort,
    redis_key,
    api_response,
    redis_response,
):
    body, status = await make_get_request(f"/api/v1/films/search?sort={sort}")
    assert status == HTTPStatus.OK
    assert body == api_response

    films_in_cache = await redis_client.get(redis_key)
    films_deserialize = orjson.loads(films_in_cache)
    assert films_deserialize == redis_response
