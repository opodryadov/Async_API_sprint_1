from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException

from src.models import Film
from src.services.film import FilmService


router = APIRouter()


@router.get(
    "/{film_id}",
    response_model=Film,
    summary="Список фильмов",
    description="Список фильмов с пагинацией, фильтрацией по жанрам и сортировкой по названию и рейтингу",
    response_description="Название фильма и его id",
)
async def film_details(
    film_id: str, film_service: FilmService = Depends(FilmService)
) -> Film:
    film = await film_service.get_by_id(film_id)
    if not film:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="film not found"
        )

    return Film(**film.dict())
