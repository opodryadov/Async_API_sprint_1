from http import HTTPStatus

import orjson
import pytest

from src.models.genre import Genre
from tests.functional.testdata.vars.films import (
    COMEDY_FILMS_RESPONSE,
    COMEDY_FILMS_IN_CACHE,
    FANTASY_FILMS_RESPONSE,
    FANTASY_FILMS_IN_CACHE,
)


pytestmark = pytest.mark.asyncio


@pytest.mark.usefixtures("flush_redis")
@pytest.mark.parametrize(
    "genre, redis_key, api_response, redis_response",
    (
        (
            Genre(id="5373d043-3f41-4ea8-9947-4b746c601bbd", name="Comedy"),
            "2e90dafa00af7f061f0878c175dbc346",
            COMEDY_FILMS_RESPONSE,
            COMEDY_FILMS_IN_CACHE,
        ),
        (
            Genre(id="b92ef010-5e4c-4fd0-99d6-41b6456272cd", name="Fantasy"),
            "536f24f4a30187e04f17067193e24764",
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
    body, status = await make_get_request(
        f"/api/v1/films?genre={genre.id}"
    )
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
