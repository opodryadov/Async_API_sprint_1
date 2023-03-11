from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException, Request

from src.models import ModelMixin
from src.services.person import PersonService


router = APIRouter()


@router.get("/search")
async def search_persons(
    request: Request,
    person_service: PersonService = Depends(PersonService),
):
    pass


class PersonAPI(ModelMixin):
    full_name: str


@router.get("/{person_id}", response_model=PersonAPI)
async def person_details(
    person_id: str,
    person_service: PersonService = Depends(PersonService),
):
    person = await person_service.get_by_id(person_id)
    if not person:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Person not found"
        )

    return PersonAPI(**person.dict(by_alias=True))


@router.get("/{person_id}/film")
async def list_film_by_person(
    request: Request,
    person_id: str,
    person_service: PersonService = Depends(PersonService),
):
    pass
