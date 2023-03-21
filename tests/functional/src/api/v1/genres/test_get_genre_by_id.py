from http import HTTPStatus

import pytest


pytestmark = pytest.mark.asyncio


async def test_get_genre_by_id(make_get_request):
    genre_id = "3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff"
    genre_name = "Action"

    body, status = await make_get_request(f"/api/v1/genres/{genre_id}")
    assert status == HTTPStatus.OK
    assert body.get("uuid") == genre_id
    assert body.get("name") == genre_name
