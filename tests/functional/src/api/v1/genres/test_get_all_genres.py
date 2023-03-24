from http import HTTPStatus

import pytest


pytestmark = pytest.mark.asyncio


async def test_get_all_genres(make_get_request):
    genre_list = (
        "Action", "Adventure", "Fantasy", "Sci-Fi",
        "Drama", "Music", "Romance", "Thriller", "Mystery",
        "Comedy", "Animation", "Family", "Biography", "Musical",
        "Crime", "Short", "Western", "Documentary", "History",
        "War", "Game-Show", "Reality-TV", "Horror", "Sport",
        "Talk-Show", "News"
    )

    body, status = await make_get_request(f"/api/v1/genres")
    assert status == HTTPStatus.OK

    genre_list_from_body = [genre.get('name') for genre in body]

    for genre in genre_list:
        assert genre in genre_list_from_body


async def test_get_422(make_get_request):
    body, status = await make_get_request(
        f"/api/v1/genres", params={"page_number": -1}
    )
    assert status == HTTPStatus.UNPROCESSABLE_ENTITY
