from http import HTTPStatus

import pytest


pytestmark = pytest.mark.asyncio


async def test_get_film_by_id(make_get_request):
    film_id = "00af52ec-9345-4d66-adbe-50eb917f463a"
    film_title = "Star Slammer"

    body, status = await make_get_request(f"/api/v1/films/{film_id}")
    assert status == HTTPStatus.OK
    assert body.get("uuid") == film_id
    assert body.get("title") == film_title
    assert body.get("imdb_rating") == 3.5
    assert len(body.get("genre")) == 3
    assert len(body.get("actors")) == 4
    assert len(body.get("writers")) == 3
    assert len(body.get("directors")) == 1

    genres = [genre["name"] for genre in body.get('genre')]
    assert "Action" in genres

    writers = [genre["full_name"] for genre in body.get('writers')]
    directors = [genre["full_name"] for genre in body.get('directors')]
    assert "Fred Olen Ray" in writers and directors
