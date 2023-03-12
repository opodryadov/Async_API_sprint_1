from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException, Request

from src.models import Person
from src.services.person import PersonService


router = APIRouter()


@router.get("/search")
async def search_persons(
    request: Request,
    person_service: PersonService = Depends(PersonService),
):
    pass


@router.get("/{person_id}", response_model=Person)
async def person_details(
    person_id: str,
    person_service: PersonService = Depends(PersonService),
) -> Person:
    person = await person_service.get_by_id(person_id)
    if not person:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Person not found"
        )

    return Person(**person.dict(by_alias=True))


@router.get("/{person_id}/film")
async def list_film_by_person(
    request: Request,
    person_id: str,
    person_service: PersonService = Depends(PersonService),
):
    pass
