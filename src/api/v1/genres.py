import logging
from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException

from src.common.utils import PaginateQueryParams
from src.models import Genre
from src.models.response import NotFound
from src.services.genre import GenreService, get_genre_service


router = APIRouter()

logger = logging.getLogger(__name__)


@router.get(
    "",
    response_model=list[Genre],
    summary="Список жанров",
    description="Список жанров",
    response_description="Весь список жанров",
)
async def list_genres(
    genre_service: GenreService = Depends(get_genre_service),
    pagination: PaginateQueryParams = Depends(),
) -> list[dict]:
    params = dict(
        page_number=pagination.page_number,
        page_size=pagination.page_size,
    )
    genres = await genre_service.get_list(params)
    if not genres:
        logger.warning("Was not a single genre")
        return []

    return genres


@router.get(
    "/{genre_id}",
    response_model=Genre,
    responses={404: {"model": NotFound}},
    summary="Получить информацию о жанре",
    description="Получить информацию о жанре",
    response_description="Подробная информация о жанре",
)
async def genre_details(
    genre_id: str,
    genre_service: GenreService = Depends(get_genre_service),
) -> dict:
    genre = await genre_service.get_by_id(genre_id)
    if not genre:
        logger.warning("Genre was not found by id %s", genre_id)
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Genre not found"
        )

    return genre
