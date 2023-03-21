from http import HTTPStatus

import pytest


pytestmark = pytest.mark.asyncio


@pytest.mark.usefixtures("flush_redis")
async def test_search(make_get_request):
    query_data = {"query": "The Star"}

    body, status = await make_get_request(
        "/api/v1/films/search/", params=query_data
    )
    assert status == HTTPStatus.OK
    assert len(body) == 50
