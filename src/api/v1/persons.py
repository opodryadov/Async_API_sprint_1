from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException, Query

from src.models import Person, PersonFilm
from src.services.person import PersonService


router = APIRouter()


@router.get("/search")
async def search_persons(
    person_service: PersonService = Depends(PersonService),
    query: str | None = Query(default=""),
    page_size: int | None = Query(default=50),
    page_number: int | None = Query(default=1),
):
    persons = await person_service.person_search(query, page_size, page_number)
    if not persons:
        return []
    return persons


@router.get("/{person_id}", response_model=Person)
async def person_details(
    person_id: str,
    person_service: PersonService = Depends(PersonService),
) -> dict:
    person = await person_service.get_person_by_id(person_id)
    if not person:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Person not found"
        )

    return person


@router.get("/{person_id}/film", response_model=list[PersonFilm])
async def list_film_by_person(
    person_id: str,
    person_service: PersonService = Depends(PersonService),
) -> list[dict]:
    films = await person_service.get_films_by_person_id(person_id)
    if not films:
        return []

    return films
