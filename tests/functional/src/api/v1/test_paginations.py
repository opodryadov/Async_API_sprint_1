from http import HTTPStatus

import pytest

from tests.functional.testdata.vars.persons import PAGINATIONS_VALIDATION


pytestmark = pytest.mark.asyncio


@pytest.mark.usefixtures("flush_redis")
@pytest.mark.parametrize(
    "endpoint",
    ("/api/v1/persons/search",),
)
@pytest.mark.parametrize(
    "page_number, page_size, records_per_page",
    (
        (1, 50, 50),
        (1, 1, 1),
    ),
)
async def test_search_persons_paginations(
    make_get_request,
    endpoint,
    page_number,
    page_size,
    records_per_page,
):
    body, status = await make_get_request(
        f"{endpoint}?page_number={page_number}&page_size={page_size}"
    )
    assert status == HTTPStatus.OK
    assert (len(body)) == records_per_page


@pytest.mark.usefixtures("flush_redis")
@pytest.mark.parametrize(
    "endpoint",
    ("/api/v1/persons/search",),
)
@pytest.mark.parametrize(
    "page_number, page_size, api_response",
    (
        (
            -1,
            50,
            PAGINATIONS_VALIDATION,
        ),
        (
            0,
            1,
            PAGINATIONS_VALIDATION,
        ),
    ),
)
async def test_search_persons_paginations_validation(
    make_get_request,
    endpoint,
    page_number,
    page_size,
    api_response,
):
    body, status = await make_get_request(
        f"{endpoint}?page_number={page_number}&page_size={page_size}"
    )
    assert status == HTTPStatus.UNPROCESSABLE_ENTITY
    assert body == api_response
