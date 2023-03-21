from http import HTTPStatus

import pytest


pytestmark = pytest.mark.asyncio


async def test_get_person_by_id(test_client):
    person_id = "dbac6947-e620-4f92-b6a1-dae9a3b07422"
    person_name = "Damon Lindelof"

    response = await test_client.get(f"/persons/{person_id}")

    assert response.status_code == HTTPStatus.OK
    body = response.json()
    assert body.get("uuid") == person_id
    assert body.get("full_name") == person_name
