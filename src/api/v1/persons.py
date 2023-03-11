from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException, Request

from src.models.base import ORDJSONModelMixin
from src.services.person import PersonService


router = APIRouter()


@router.get("/search")
async def search_persons(
    request: Request,
    person_service: PersonService = Depends(PersonService),
):
    pass


class PersonAPI(ORDJSONModelMixin):
    uuid: str
    full_name: str
    # role: str
    # film_ids: list[str] | None = Field(default=list())


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
