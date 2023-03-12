from http import HTTPStatus

import pytest

from tests.vars.persons import MockElastic, MockRedis


pytestmark = pytest.mark.asyncio


async def test_get_person_by_id(test_client, monkeypatch):
    person_id = "00395304-dd52-4c7b-be0d-c2cd7a495684"

    mocker_redis = MockRedis()
    mocker_redis.add_mock_get(monkeypatch, person_id=person_id, in_cache=False)
    mocker_es = MockElastic()
    mocker_es.add_mock_get(monkeypatch, person_id=person_id)
    response = await test_client.get(f"/api/v1/persons/{person_id}")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "uuid": person_id,
        "full_name": "Jennifer Hale",
        "role": "actor",
        "film_ids": [
            "32064806-8196-4037-b758-dd5b5d274b59",
            "2a090dde-f688-46fe-a9f4-b781a985275e",
            "4fdffe40-e77f-4fb2-96ad-47319e3ddd2a",
            "c4d36327-b330-4506-a63d-fef69d3f2f8a",
        ],
    }

    mocker_redis = MockRedis()
    mocker_redis.add_mock_get(monkeypatch, person_id=person_id)
    mocker_es = MockElastic()
    mocker_es.add_mock_get(monkeypatch, person_id=person_id, in_es=False)
    response = await test_client.get(f"/api/v1/persons/{person_id}")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "uuid": person_id,
        "full_name": "Jennifer Hale",
        "role": "actor",
        "film_ids": [
            "32064806-8196-4037-b758-dd5b5d274b59",
            "2a090dde-f688-46fe-a9f4-b781a985275e",
            "4fdffe40-e77f-4fb2-96ad-47319e3ddd2a",
            "c4d36327-b330-4506-a63d-fef69d3f2f8a",
        ],
    }
