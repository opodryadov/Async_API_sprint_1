import logging
from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException, Query

from src.common.utils import PaginateQueryParams
from src.models import Person, PersonFilm
from src.models.response import NotFound
from src.services.person import PersonService, get_person_service


router = APIRouter()

logger = logging.getLogger(__name__)


@router.get(
    "/search",
    response_model=list[Person],
    summary="Поиск по персонам",
    description="Поиск по персонам",
    response_description="Результат поиска",
)
async def search_persons(
    query: str
    | None = Query(
        "",
        title="Имя/фамилия для поиска",
        description="Поиск по имени/фамилии",
    ),
    pagination: PaginateQueryParams = Depends(),
    person_service: PersonService = Depends(get_person_service),
) -> list[dict]:
    params = dict(
        query=query,
        page_number=pagination.page_number,
        page_size=pagination.page_size,
    )
    persons = await person_service.person_search(params)
    if not persons:
        return []
    return persons


@router.get(
    "/{person_id}",
    response_model=Person,
    responses={404: {"model": NotFound}},
    summary="Получить информацию о персоне",
    description="Получить информацию о персоне",
    response_description="Подробная информация о персоне",
)
async def person_details(
    person_id: str,
    person_service: PersonService = Depends(get_person_service),
) -> dict:
    person = await person_service.get_person_by_id(person_id)
    if not person:
        logger.warning("Person was not found by id %s", person_id)
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Person not found"
        )

    return person


@router.get(
    "/{person_id}/film",
    response_model=list[PersonFilm],
    responses={404: {"model": NotFound}},
    summary="Получить фильмы по персоне",
    description="Получить фильмы по персоне",
    response_description="Фильмы по персоне",
)
async def list_film_by_person(
    person_id: str,
    person_service: PersonService = Depends(get_person_service),
) -> list[dict]:
    films = await person_service.get_films_by_person_id(person_id)
    if not films:
        logger.info(
            "Person did not participate in any film: person_id %s", person_id
        )
        return []

    return films
