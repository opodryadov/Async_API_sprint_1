import datetime
import json
import uuid
from http import HTTPStatus

import pytest


pytestmark = pytest.mark.asyncio


async def test_search(test_client):
    query_data = {"query": "The Star"}
    response = await test_client.get("/api/v1/films/search", params=query_data)

    assert response.status_code == HTTPStatus.OK
    assert len(response.json()) == 50
