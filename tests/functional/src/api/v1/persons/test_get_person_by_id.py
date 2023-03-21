from http import HTTPStatus

import pytest


pytestmark = pytest.mark.asyncio


async def test_get_person_by_id(make_get_request):
    person_id = "dbac6947-e620-4f92-b6a1-dae9a3b07422"
    person_name = "Damon Lindelof"

    body, status = await make_get_request(f"/api/v1/persons/{person_id}")
    assert status == HTTPStatus.OK
    assert body.get("uuid") == person_id
    assert body.get("full_name") == person_name
