import logging
from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException

from src.common.utils import query_params
from src.models import Person, PersonFilm
from src.models.response import BadRequest, NotFound
from src.services.person import PersonService


router = APIRouter()

logger = logging.getLogger(__name__)


@router.get(
    "/search",
    response_model=list[Person],
    summary="Поиск по персонам",
    description="Поиск по персонам.",
    response_description="Результат поиска.",
)
async def search_persons(
    person_service: PersonService = Depends(PersonService),
    params: dict = Depends(query_params),
) -> list[dict]:
    persons = await person_service.person_search(params)
    if not persons:
        return []
    return persons


@router.get(
    "/{person_id}",
    response_model=Person,
    responses={404: {"model": NotFound}, 400: {"model": BadRequest}},
    summary="Получить информацию о персоне",
    description="Получить информацию о персоне.",
    response_description="Подробная информация о персоне.",
)
async def person_details(
    person_id: str,
    person_service: PersonService = Depends(PersonService),
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
    responses={404: {"model": NotFound}, 400: {"model": BadRequest}},
    summary="Получить фильмы по персоне",
    description="Получить фильмы по персоне.",
    response_description="Фильмы по персоне.",
)
async def list_film_by_person(
    person_id: str,
    person_service: PersonService = Depends(PersonService),
) -> list[dict]:
    films = await person_service.get_films_by_person_id(person_id)
    if not films:
        logger.info(
            "Person did not participate in any film: person_id %s", person_id
        )
        return []

    return films
