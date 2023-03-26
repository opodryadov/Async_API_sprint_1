from http import HTTPStatus

import orjson
import pytest

from tests.functional.testdata.vars.persons import (
    CACHE_PERSON_ACTOR_FILMS,
    CACHE_PERSON_WRITER_DIRECTOR_FILMS_1,
    CACHE_PERSON_WRITER_DIRECTOR_FILMS_2,
    CACHE_PERSON_WRITER_FILMS,
    PERSON_ACTOR_FILMS,
    PERSON_NOT_IN_FILMS,
    PERSON_WRITER_DIRECTOR_FILMS,
    PERSON_WRITER_FILMS,
)


pytestmark = pytest.mark.asyncio


@pytest.mark.usefixtures("flush_redis")
@pytest.mark.parametrize(
    "person_id, api_response, key_directors, key_writers, key_actors, cache_directors, cache_writers, cache_actors",
    (
        (
            "dbac6947-e620-4f92-b6a1-dae9a3b07422",
            PERSON_WRITER_FILMS,
            "1dcb2c84e354e33720a9b9c81457fd4a",
            "304c29f32b5d34f0150fd10f6f9af2f4",
            "98c2f1ad27044e36787cca8c25ffae2d",
            [],
            CACHE_PERSON_WRITER_FILMS,
            [],
        ),
        (
            "00395304-dd52-4c7b-be0d-c2cd7a495684",
            PERSON_ACTOR_FILMS,
            "41f1d4027238c414b315cc541c24a172",
            "934a2152e04bfbb3228a6b0004fc4590",
            "943fdfb0c544026490dcad384c6aa611",
            [],
            [],
            CACHE_PERSON_ACTOR_FILMS,
        ),
        (
            "b66db341-5dcd-4aaf-b536-050b59979357",
            PERSON_WRITER_DIRECTOR_FILMS,
            "32e6d535767afb7b767ed0884df2e4a0",
            "2cd9e3be9cbce0f0614400da7a0d6658",
            "75fac9e3da31fec7258817f4634109be",
            CACHE_PERSON_WRITER_DIRECTOR_FILMS_1,
            CACHE_PERSON_WRITER_DIRECTOR_FILMS_2,
            [],
        ),
        (
            "a5a8f573-3cee-4c3v-8a2b-91cb9f55250a",
            PERSON_NOT_IN_FILMS,
            "955f3474cd5fa9a7fded453c8c8afd81",
            "aa17956d47133eb428bcf24e61e18001",
            "0cf2bb2e826d9c86781f5b3643a53daf",
            [],
            [],
            [],
        ),
        (
            "test_person_not_found_id",
            PERSON_NOT_IN_FILMS,
            "469034b2a6b094985cb2972a4dee8a29",
            "b007329311a2fd289d42527c1b8fc59a",
            "2909d04882fe111e64871209d6b36bf0",
            [],
            [],
            [],
        ),
    ),
)
async def test_list_film_by_person(
    make_get_request,
    redis_client,
    person_id,
    api_response,
    key_directors,
    key_writers,
    key_actors,
    cache_directors,
    cache_writers,
    cache_actors,
):
    body, status = await make_get_request(f"/api/v1/persons/{person_id}/film")
    assert status == HTTPStatus.OK
    assert body == api_response

    films_director_in_chache = await redis_client.get(key_directors)
    if films_director_in_chache:
        person_deserealize = orjson.loads(films_director_in_chache)
        assert person_deserealize == cache_directors

    films_writer_in_chache = await redis_client.get(key_writers)
    if films_writer_in_chache:
        person_deserealize = orjson.loads(films_writer_in_chache)
        assert person_deserealize == cache_writers

    films_actor_in_chache = await redis_client.get(key_actors)
    if films_actor_in_chache:
        person_deserealize = orjson.loads(films_actor_in_chache)
        assert person_deserealize == cache_actors
