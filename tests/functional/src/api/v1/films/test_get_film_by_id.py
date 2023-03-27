from http import HTTPStatus

import orjson
import pytest

from tests.functional.testdata.vars.films import (
    FILM_INFO,
    FILM_INFO_CACHE,
    FILM_WITHOUT_RATING_AND_PERSONS,
    FILM_WITHOUT_RATING_AND_PERSONS_CACHE,
)


pytestmark = pytest.mark.asyncio


@pytest.mark.usefixtures("flush_redis")
@pytest.mark.parametrize(
    "film_id, api_response, redis_response",
    (
        (
            "27b726f2-40e9-4d81-b608-57f7c41bfe54",
            FILM_INFO,
            FILM_INFO_CACHE,
        ),
        (
            "32fcd689-3119-4225-8076-fdeabc553c61",
            FILM_WITHOUT_RATING_AND_PERSONS,
            FILM_WITHOUT_RATING_AND_PERSONS_CACHE,
        ),
    ),
)
async def test_get_film_by_id(
    make_get_request, redis_client, film_id, api_response, redis_response
):
    body, status = await make_get_request(f"/api/v1/films/{film_id}")
    assert status == HTTPStatus.OK
    assert body == api_response

    films_in_cache = await redis_client.get(film_id)
    films_deserialize = orjson.loads(films_in_cache)
    assert films_deserialize == redis_response


async def test_get_film_not_found(make_get_request, redis_client):
    unknown_film_id = "96dad231-e626-420c-b076-c71ec012ef63"

    body, status = await make_get_request(f"/api/v1/films/{unknown_film_id}")
    assert status == HTTPStatus.NOT_FOUND
    assert body == {"detail": "Film not found"}

    film_in_cache = await redis_client.get(unknown_film_id)
    assert film_in_cache is None
