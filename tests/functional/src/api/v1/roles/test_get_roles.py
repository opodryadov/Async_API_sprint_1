from http import HTTPStatus

import pytest

from tests.functional.core import test_settings
from tests.functional.testdata.vars.roles import GET_ALL_ROLES_RESPONSE


pytestmark = pytest.mark.asyncio


async def test_get_all_roles_ok(
    test_client, monkeypatch, mock_auth_api_list_roles_ok
):
    res = await test_client.get(
        "/api/v1/roles", headers={"X-TOKEN": test_settings.auth_api_srv_token}
    )
    assert res.status_code == HTTPStatus.OK
    body = res.json()
    assert body == GET_ALL_ROLES_RESPONSE.get("result")
