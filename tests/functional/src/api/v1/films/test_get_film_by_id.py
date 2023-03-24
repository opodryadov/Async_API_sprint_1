import json
from http import HTTPStatus

import pytest


pytestmark = pytest.mark.asyncio

film_id = "00af52ec-9345-4d66-adbe-50eb917f463a"
film_title = "Star Slammer"
unknown_film_id = "96dad231-e626-420c-b076-c71ec012ef63"


@pytest.mark.usefixtures("flush_redis")
async def test_get_film_by_id(make_get_request, redis_client):
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

    data = await redis_client.get(name=film_id)
    assert data is not None

    data = json.loads(data)
    assert data.get("id") == film_id
    assert data.get("title") == film_title


async def test_get_404(make_get_request):
    body, status = await make_get_request(
        f"/api/v1/films/{unknown_film_id}"
    )
    assert status == HTTPStatus.NOT_FOUND
