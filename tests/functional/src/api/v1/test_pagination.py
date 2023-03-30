from http import HTTPStatus

import pytest

from tests.functional.testdata.vars.pagination import (
    PAGINATION_VALIDATION_PAGE_NUMBER,
    PAGINATION_VALIDATION_PAGE_SIZE,
    PAGINATION_VALIDATION_PAGE_SIZE_NOT_GE,
)


pytestmark = pytest.mark.asyncio


@pytest.mark.usefixtures("flush_redis")
@pytest.mark.parametrize(
    "endpoint",
    (
        "persons/search",
        "films",
        "films/search",
    ),
)
@pytest.mark.parametrize(
    "page_number, page_size, records_per_page",
    (
        (1, 50, 50),
        (1, 1, 1),
    ),
)
async def test_search_pagination(
    make_get_request,
    endpoint,
    page_number,
    page_size,
    records_per_page,
):
    body, status = await make_get_request(
        f"/api/v1/{endpoint}?page_number={page_number}&page_size={page_size}"
    )
    assert status == HTTPStatus.OK
    assert (len(body)) == records_per_page


@pytest.mark.usefixtures("flush_redis")
@pytest.mark.parametrize(
    "page_number, page_size, records_per_page",
    (
        (1, 26, 26),
        (1, 1, 1),
    ),
)
async def test_genres_pagination(
    make_get_request,
    page_number,
    page_size,
    records_per_page,
):
    body, status = await make_get_request(
        f"/api/v1/genres?page_number={page_number}&page_size={page_size}"
    )
    assert status == HTTPStatus.OK
    assert (len(body)) == records_per_page


@pytest.mark.usefixtures("flush_redis")
@pytest.mark.parametrize(
    "endpoint",
    ("persons/search", "genres", "films", "films/search"),
)
@pytest.mark.parametrize(
    "page_number, page_size, api_response",
    (
        (
            -1,
            50,
            PAGINATION_VALIDATION_PAGE_NUMBER,
        ),
        (
            0,
            1,
            PAGINATION_VALIDATION_PAGE_NUMBER,
        ),
        (
            1,
            501,
            PAGINATION_VALIDATION_PAGE_SIZE,
        ),
        (
            1,
            0,
            PAGINATION_VALIDATION_PAGE_SIZE_NOT_GE,
        ),
        (
            1,
            -1,
            PAGINATION_VALIDATION_PAGE_SIZE_NOT_GE,
        ),
    ),
)
async def test_search_pagination_validation(
    make_get_request,
    endpoint,
    page_number,
    page_size,
    api_response,
):
    body, status = await make_get_request(
        f"/api/v1/{endpoint}?page_number={page_number}&page_size={page_size}"
    )
    assert status == HTTPStatus.UNPROCESSABLE_ENTITY
    assert body == api_response
