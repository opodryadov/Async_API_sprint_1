from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException, Query

from src.common.utils import query_params
from src.models import Film, FilmShort
from src.models.response import NotFound
from src.services.film import FilmService, get_film_service


router = APIRouter()


@router.get(
    "/",
    response_model=list[FilmShort],
    summary="Список фильмов",
    description="Список фильмов с пагинацией, фильтрацией по жанрам и сортировкой по названию и рейтингу",
    response_description="Список фильмов с UUID, названием и рейтингом",
)
async def list_films(
    params: dict = Depends(query_params),
    genre: str | None = Query(default=""),
    film_service: FilmService = Depends(get_film_service),
) -> list[FilmShort]:
    films = await film_service.get_all_films(params, genre)
    if not films:
        return []

    return films


@router.get(
    "/search",
    response_model=list[FilmShort],
    summary="Поиск по фильмам",
    description="Поиск по фильмам",
    response_description="Результат поиска",
)
async def search_films(
    params: dict = Depends(query_params),
    film_service: FilmService = Depends(get_film_service),
) -> list[FilmShort]:
    films = await film_service.search_films(params)
    if not films:
        return []

    return films


@router.get(
    "/{film_id}",
    response_model=Film,
    summary="Получить информацию по фильму",
    description="Получить информацию по фильму",
    responses={404: {"model": NotFound}},
    response_description="Подробная информация о фильме",
)
async def film_details(
    film_id: str, film_service: FilmService = Depends(get_film_service)
) -> dict:
    film = await film_service.get_by_id(film_id)
    if not film:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Film not found"
        )

    return film
