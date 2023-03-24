import json
from http import HTTPStatus

import pytest


pytestmark = pytest.mark.asyncio


@pytest.mark.usefixtures("flush_redis")
async def test_get_genre_by_id(make_get_request, redis_client):
    genre_id = "3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff"
    genre_name = "Action"

    body, status = await make_get_request(f"/api/v1/genres/{genre_id}")
    assert status == HTTPStatus.OK
    assert body.get("uuid") == genre_id
    assert body.get("name") == genre_name

    data = await redis_client.get(name=genre_id)
    assert data is not None

    data = json.loads(data)
    assert data.get("id") == genre_id
    assert data.get("name") == genre_name


async def test_get_404(make_get_request):
    body, status = await make_get_request(
        f"/api/v1/genres/96dad231-e626-420c-b076-c71ec012ef63"
    )
    assert status == HTTPStatus.NOT_FOUND
