from http import HTTPStatus

import pytest


pytestmark = pytest.mark.asyncio


@pytest.mark.usefixtures("flush_redis")
async def test_get_all_genres(make_get_request, redis_client):
    redis_key = "bff0b4bf49e1bf3ff01d8b1fc8a11ca1"
    params = {"page_number": 1, "page_size": 50}
    genre_list = (
        "Action", "Adventure", "Fantasy", "Sci-Fi",
        "Drama", "Music", "Romance", "Thriller", "Mystery",
        "Comedy", "Animation", "Family", "Biography", "Musical",
        "Crime", "Short", "Western", "Documentary", "History",
        "War", "Game-Show", "Reality-TV", "Horror", "Sport",
        "Talk-Show", "News"
    )

    body, status = await make_get_request(
        f"/api/v1/genres", params=params
    )
    assert status == HTTPStatus.OK

    genre_list_from_body = [genre.get('name') for genre in body]

    for genre in genre_list:
        assert genre in genre_list_from_body

    data = await redis_client.get(name=redis_key)
    assert data is not None


async def test_get_422(make_get_request):
    body, status = await make_get_request(
        f"/api/v1/genres", params={"page_number": -1}
    )
    assert status == HTTPStatus.UNPROCESSABLE_ENTITY
