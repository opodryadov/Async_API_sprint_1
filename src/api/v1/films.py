from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException, Query

from src.common.collections import get_in
from src.common.decode_auth_token import get_decoded_data
from src.common.utils import PaginateQueryParams, get_sort
from src.models import Film, FilmShort
from src.models.response import NotFound
from src.models.role import RoleType
from src.services.film import FilmService, get_film_service


router = APIRouter()


@router.get(
    "",
    response_model=list[FilmShort],
    summary="Список фильмов",
    description="Список фильмов с фильтрацией по жанрам",
    response_description="Список фильмов",
)
async def list_films(
    genre: str
    | None = Query(
        "",
        title="UUID жанра",
        description="UUID жанра",
    ),
    sort: str
    | None = Query(
        "",
        title="Сортировка",
        description="Сортировка (имя/рейтинг)",
    ),
    pagination: PaginateQueryParams = Depends(),
    film_service: FilmService = Depends(get_film_service),
) -> list[FilmShort]:
    params = dict(
        genre=genre,
        sort=get_sort(sort),
        page_number=pagination.page_number,
        page_size=pagination.page_size,
    )
    films = await film_service.get_all_films(params)
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
    query: str
    | None = Query(
        "",
        title="Слово для поиска",
        description="Поиск по слову в названии/описании",
    ),
    sort: str
    | None = Query(
        default="",
        title="Сортировка",
        description="Сортировка (имя/рейтинг)",
    ),
    pagination: PaginateQueryParams = Depends(),
    film_service: FilmService = Depends(get_film_service),
) -> list[FilmShort]:
    params = dict(
        query=query,
        sort=get_sort(sort),
        page_number=pagination.page_number,
        page_size=pagination.page_size,
    )
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
    film_id: str,
    film_service: FilmService = Depends(get_film_service),
    user_data=Depends(get_decoded_data),
) -> dict:
    roles = get_in(user_data, "roles")
    if not roles or RoleType.ROLE_SUBSCRIBER not in roles:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN,
            detail="No access to watching films",
        )
    film = await film_service.get_by_id(film_id)
    if not film:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Film not found"
        )

    return film
