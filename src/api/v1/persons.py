from fastapi import APIRouter, Depends, Request

from src.services.person import PersonService, get_person_service


router = APIRouter()


@router.get("/search")
async def search_persons(
    request: Request,
    person_service: PersonService = Depends(get_person_service),
):
    pass


@router.get("/{person_id}")
async def person_details(
    request: Request,
    person_id: str,
    person_service: PersonService = Depends(get_person_service),
):
    pass


@router.get("/{person_id}/film")
async def list_film_by_person(
    request: Request,
    person_id: str,
    person_service: PersonService = Depends(get_person_service),
):
    pass
