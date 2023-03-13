from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException

from src.models import Film, FilmShort
from src.services.film import FilmService


router = APIRouter()


def get_sort(field: str) -> dict:
    if not field or field not in \
            ("title", "-title", "imdb_rating", "-imdb_rating"):
        return {}

    method = "desc" if "-" in field else "asc"
    field = field.replace("-", "")
    if "title" in field:
        field = field.replace("title", "title.raw")

    return {field: method}


@router.get(
    "/",
    response_model=list[FilmShort],
    summary="Список фильмов",
    description="Список фильмов с пагинацией, фильтрацией по жанрам и сортировкой по названию и рейтингу",
    response_description="Список фильмов с UUID, названием и рейтингом"
)
async def all_films_details(
    genre: str = "",
    sort: str = "",
    page_number: int = 0,
    page_size: int = 10,
    film_service: FilmService = Depends(FilmService)
) -> list[Film]:
    films = await film_service.get_all_films(
        genre_uuid=genre,
        sort=get_sort(sort),
        page_size=page_size,
        page_number=page_number
    )
    if not films:
        return []

    return films


@router.get(
    "/{film_id}",
    response_model=Film,
    summary="Информация по фильму",
    description="Полная информация по фильму",
    response_description="UUID, название, рейтинг, описание, жанр, актёры, сценаристы, режиссёры",
)
async def film_details(
    film_id: str,
    film_service: FilmService = Depends(FilmService)
) -> Film:
    film = await film_service.get_by_id(film_id)
    if not film:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="film not found"
        )

    return Film(**film.dict())
