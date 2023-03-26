from http import HTTPStatus

import orjson
import pytest

from tests.functional.testdata.vars.persons import (
    CACHE_PERSON_ACTOR,
    CACHE_PERSON_NOT_ROLE,
    CACHE_PERSON_WRITER,
    CACHE_PERSON_WRITER_DIRECTOR,
    PERSON_ACTOR,
    PERSON_NOT_ROLE,
    PERSON_WRITER,
    PERSON_WRITER_DIRECTOR,
)


pytestmark = pytest.mark.asyncio


@pytest.mark.usefixtures("flush_redis")
@pytest.mark.parametrize(
    "person_id, api_response, redis_response",
    (
        (
            "dbac6947-e620-4f92-b6a1-dae9a3b07422",
            PERSON_WRITER,
            CACHE_PERSON_WRITER,
        ),
        (
            "00395304-dd52-4c7b-be0d-c2cd7a495684",
            PERSON_ACTOR,
            CACHE_PERSON_ACTOR,
        ),
        (
            "b66db341-5dcd-4aaf-b536-050b59979357",
            PERSON_WRITER_DIRECTOR,
            CACHE_PERSON_WRITER_DIRECTOR,
        ),
        (
            "a5a8f573-3cee-4c3v-8a2b-91cb9f55250a",
            PERSON_NOT_ROLE,
            CACHE_PERSON_NOT_ROLE,
        ),
    ),
)
async def test_get_person_by_id(
    make_get_request, redis_client, person_id, api_response, redis_response
):
    body, status = await make_get_request(f"/api/v1/persons/{person_id}")
    assert status == HTTPStatus.OK
    assert body == api_response

    person_in_chache = await redis_client.get(person_id)
    person_deserialize = orjson.loads(person_in_chache)
    assert person_deserialize == redis_response


async def test_get_person_not_found(make_get_request, redis_client):
    person_id = "test_bad_id"

    body, status = await make_get_request(f"/api/v1/persons/{person_id}")
    assert status == HTTPStatus.NOT_FOUND
    assert body == {"detail": "Person not found"}

    person_in_chache = await redis_client.get(person_id)
    assert person_in_chache is None
