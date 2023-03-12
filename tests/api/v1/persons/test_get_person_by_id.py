from http import HTTPStatus

import pytest

from src.models import Person
from tests.vars.persons import MockPersonService


pytestmark = pytest.mark.asyncio


async def test_get_person_by_id(test_client, monkeypatch):
    person_id = "00395304-dd52-4c7b-be0d-c2cd7a495684"
    full_name = "Jennifer Hale"
    person = Person(id=person_id, full_name=full_name)

    mocker_person_service = MockPersonService()
    mocker_person_service.add_mock_person_from_cache(
        monkeypatch, person_id=person_id, in_cache=False
    )
    mocker_person_service.add_mock_get_person_elastic(
        monkeypatch, person_id=person_id
    )
    mocker_person_service.add_mock_enrich(monkeypatch, person)
    response = await test_client.get(f"/api/v1/persons/{person_id}")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "films": [
            {
                "roles": ["actor"],
                "uuid": "2a090dde-f688-46fe-a9f4-b781a985275e",
            },
            {
                "roles": ["actor"],
                "uuid": "32064806-8196-4037-b758-dd5b5d274b59",
            },
            {
                "roles": ["actor"],
                "uuid": "4fdffe40-e77f-4fb2-96ad-47319e3ddd2a",
            },
            {
                "roles": ["actor"],
                "uuid": "c4d36327-b330-4506-a63d-fef69d3f2f8a",
            },
        ],
        "full_name": "Jennifer Hale",
        "uuid": "00395304-dd52-4c7b-be0d-c2cd7a495684",
    }

    mocker_person_service = MockPersonService()
    mocker_person_service.add_mock_person_from_cache(
        monkeypatch, person_id=person_id
    )
    mocker_person_service.add_mock_get_person_elastic(
        monkeypatch, person_id=person_id, in_es=False
    )
    response = await test_client.get(f"/api/v1/persons/{person_id}")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "films": [
            {
                "roles": ["actor"],
                "uuid": "2a090dde-f688-46fe-a9f4-b781a985275e",
            },
            {
                "roles": ["actor"],
                "uuid": "32064806-8196-4037-b758-dd5b5d274b59",
            },
            {
                "roles": ["actor"],
                "uuid": "4fdffe40-e77f-4fb2-96ad-47319e3ddd2a",
            },
            {
                "roles": ["actor"],
                "uuid": "c4d36327-b330-4506-a63d-fef69d3f2f8a",
            },
        ],
        "full_name": "Jennifer Hale",
        "uuid": "00395304-dd52-4c7b-be0d-c2cd7a495684",
    }
