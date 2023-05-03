from http import HTTPStatus

import pytest

from tests.functional.core import test_settings


pytestmark = pytest.mark.asyncio

GET_ALL_ROLES_RESPONSE = {
    "error": None,
    "result": [
        {
            "name": "ROLE_PORTAL_ADMIN",
            "role_id": "3f50d257-66da-4532-b64f-f4999282f4d0",
        },
        {
            "name": "ROLE_PORTAL_USER",
            "role_id": "5eff1f88-8f2b-40c5-a4d0-85893cb7071b",
        },
    ],
    "success": True,
}


async def test_get_all_roles_ok(test_client, monkeypatch, mock_auth_api_ok):
    res = await test_client.get(
        "/api/v1/roles", headers={"X-TOKEN": test_settings.auth_api_srv_token}
    )
    assert res.status_code == HTTPStatus.OK
    body = res.json()
    assert body == GET_ALL_ROLES_RESPONSE.get("result")
