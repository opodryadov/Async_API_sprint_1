from http import HTTPStatus

import pytest


pytestmark = pytest.mark.asyncio


async def test_get_genre_by_id(test_client):
    genre_id = "3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff"
    genre_name = "Action"

    response = await test_client.get(f"/genres/{genre_id}")

    assert response.status_code == HTTPStatus.OK
    body = response.json()
    assert body.get("uuid") == genre_id
    assert body.get("name") == genre_name
