from http import HTTPStatus

import pytest

from tests.vars.genres import MockGenreService


pytestmark = pytest.mark.asyncio


async def test_get_genre_by_id(test_client, monkeypatch):
    genre_id = "55c723c1-6d90-4a04-a44b-e9792040251a"

    mocker_genre_service = MockGenreService()
    mocker_genre_service.add_mock_genre_from_cache(
        monkeypatch, genre_id=genre_id, in_cache=False
    )
    mocker_genre_service.add_mock_get_genre_elastic(
        monkeypatch, genre_id=genre_id
    )
    response = await test_client.get(f"/api/v1/genres/{genre_id}")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "uuid": "55c723c1-6d90-4a04-a44b-e9792040251a",
        "name": "Family",
    }

    mocker_genre_service = MockGenreService()
    mocker_genre_service.add_mock_genre_from_cache(
        monkeypatch, genre_id=genre_id
    )
    mocker_genre_service.add_mock_get_genre_elastic(
        monkeypatch, genre_id=genre_id, in_es=False
    )
    response = await test_client.get(f"/api/v1/genres/{genre_id}")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "uuid": "55c723c1-6d90-4a04-a44b-e9792040251a",
        "name": "Family",
    }
