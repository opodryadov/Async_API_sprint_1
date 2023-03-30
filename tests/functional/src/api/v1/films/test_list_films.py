from http import HTTPStatus

import orjson
import pytest

from src.models.genre import Genre
from tests.functional.testdata.vars.films import (
    COMEDY_FILMS_IN_CACHE,
    COMEDY_FILMS_RESPONSE,
    FANTASY_FILMS_IN_CACHE,
    FANTASY_FILMS_RESPONSE,
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
    "genre, redis_key, api_response, redis_response",
    (
        (
            Genre(id="5373d043-3f41-4ea8-9947-4b746c601bbd", name="Comedy"),
            "movies::FilmRedisStorage::5373d043-3f41-4ea8-9947-4b746c601bbd::1::50::films_genre",
            COMEDY_FILMS_RESPONSE,
            COMEDY_FILMS_IN_CACHE,
        ),
        (
            Genre(id="b92ef010-5e4c-4fd0-99d6-41b6456272cd", name="Fantasy"),
            "movies::FilmRedisStorage::b92ef010-5e4c-4fd0-99d6-41b6456272cd::1::50::films_genre",
            FANTASY_FILMS_RESPONSE,
            FANTASY_FILMS_IN_CACHE,
        ),
    ),
)
async def test_list_film_by_genre(
    make_get_request,
    redis_client,
    es_client,
    genre,
    redis_key,
    api_response,
    redis_response,
):
    body, status = await make_get_request(f"/api/v1/films?genre={genre.id}")
    assert status == HTTPStatus.OK
    assert body == api_response

    for i in range(0, -2, -1):
        documents = await es_client.get(index="movies", id=body[i]["uuid"])
        docs = [i for i in documents["_source"]["genre"]]
        assert genre in docs

    films_in_cache = await redis_client.get(redis_key)
    films_deserialize = orjson.loads(films_in_cache)
    assert films_deserialize == redis_response


async def test_list_film_unknown_genre(make_get_request, redis_client):
    genre_id = "af4efbdc-4d14-4e4f-ae64-f023ca02fb52"

    body, status = await make_get_request(f"/api/v1/films?genre={genre_id}")
    assert status == HTTPStatus.OK
    assert body == []

    genre_in_cache = await redis_client.get(genre_id)
    assert genre_in_cache is None


@pytest.mark.usefixtures("flush_redis")
@pytest.mark.parametrize(
    "sort, redis_key, api_response, redis_response",
    (
        (
            "title",
            "movies::FilmRedisStorage::{'title.raw': 'asc'}::1::50::films_genre",
            SORT_FILMS_BY_TITLE_ASC_RESPONSE,
            SORT_FILMS_BY_TITLE_ASC_IN_CACHE,
        ),
        (
            "-title",
            "movies::FilmRedisStorage::{'title.raw': 'desc'}::1::50::films_genre",
            SORT_FILMS_BY_TITLE_DESC_RESPONSE,
            SORT_FILMS_BY_TITLE_DESC_IN_CACHE,
        ),
        (
            "imdb_rating",
            "movies::FilmRedisStorage::{'imdb_rating': 'asc'}::1::50::films_genre",
            SORT_FILMS_BY_RATING_ASC_RESPONSE,
            SORT_FILMS_BY_RATING_ASC_IN_CACHE,
        ),
        (
            "-imdb_rating",
            "movies::FilmRedisStorage::{'imdb_rating': 'desc'}::1::50::films_genre",
            SORT_FILMS_BY_RATING_DESC_RESPONSE,
            SORT_FILMS_BY_RATING_DESC_IN_CACHE,
        ),
        (
            "",
            "movies::FilmRedisStorage::1::50::films_genre",
            FILMS_WITHOUT_SORT_RESPONSE,
            FILMS_WITHOUT_SORT_IN_CACHE,
        ),
        (
            "unknown",
            "movies::FilmRedisStorage::1::50::films_genre",
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
    body, status = await make_get_request(f"/api/v1/films?sort={sort}")
    assert status == HTTPStatus.OK
    assert body == api_response

    films_in_cache = await redis_client.get(redis_key)
    films_deserialize = orjson.loads(films_in_cache)
    assert films_deserialize == redis_response
