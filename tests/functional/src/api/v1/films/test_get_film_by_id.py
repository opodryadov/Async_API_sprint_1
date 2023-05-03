from http import HTTPStatus

import orjson
import pytest

from tests.functional.testdata.vars.films import (
    FILM_INFO,
    FILM_INFO_CACHE,
    FILM_WITHOUT_RATING_AND_PERSONS,
    FILM_WITHOUT_RATING_AND_PERSONS_CACHE,
)
from tests.functional.utils.auth import TEST_PUBLIC_KEY, sign_jwt


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
    test_client,
    redis_client,
    film_id,
    api_response,
    redis_response,
    monkeypatch,
):
    monkeypatch.setattr("src.core.auth.JWT_SECRET", TEST_PUBLIC_KEY)
    test_client.cookies["access_token_cookie"] = sign_jwt(
        user_id="5f50d666-66da-4532-b64f-f4999282f4d0",
        roles=["ROLE_PORTAL_USER", "ROLE_SUBSCRIBER"],
    )
    response = await test_client.get(f"/api/v1/films/{film_id}")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == api_response

    films_in_cache = await redis_client.get(film_id)
    films_deserialize = orjson.loads(films_in_cache)
    assert films_deserialize == redis_response


async def test_get_film_not_found(redis_client, monkeypatch, test_client):
    unknown_film_id = "96dad231-e626-420c-b076-c71ec012ef63"

    monkeypatch.setattr("src.core.auth.JWT_SECRET", TEST_PUBLIC_KEY)
    test_client.cookies["access_token_cookie"] = sign_jwt(
        user_id="123",
        roles=["ROLE_SUBSCRIBER"],
    )
    response = await test_client.get(f"/api/v1/films/{unknown_film_id}")
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "Film not found"}

    film_in_cache = await redis_client.get(unknown_film_id)
    assert film_in_cache is None


async def test_get_film_forbidden(redis_client, monkeypatch, test_client):
    unknown_film_id = "96dad231-e626-420c-b076-c71ec012ef63"

    monkeypatch.setattr("src.core.auth.JWT_SECRET", TEST_PUBLIC_KEY)
    test_client.cookies["access_token_cookie"] = sign_jwt(
        user_id="123",
        roles=[
            "ROLE_PORTAL_USER",
        ],
    )
    response = await test_client.get(f"/api/v1/films/{unknown_film_id}")
    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {"detail": "No access to watching films"}

    film_in_cache = await redis_client.get(unknown_film_id)
    assert film_in_cache is None
