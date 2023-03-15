import logging
from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException, Query

from src.models import Genre
from src.models.response import BadRequest, NotFound
from src.services.genre import GenreService


router = APIRouter()

logger = logging.getLogger(__name__)


@router.get(
    "/{genre_id}",
    response_model=Genre,
    responses={404: {"model": NotFound}, 400: {"model": BadRequest}},
    summary="Получить информацию о жанре",
    description="Получить информацию о жанре.",
    response_description="Подробная информация о жанре.",
)
async def genre_details(
    genre_id: str,
    genre_service: GenreService = Depends(GenreService),
) -> dict:
    genre = await genre_service.get_genre_by_id(genre_id)
    if not genre:
        logger.warning("Genre was not found by id %s", genre_id)
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Genre not found"
        )

    return genre


@router.get(
    "/",
    response_model=list[Genre],
    summary="Список жанров",
    description="Список жанров.",
    response_description="Весь список жанров.",
)
async def list_genres(
    genre_service: GenreService = Depends(GenreService),
    page_number: int | None = Query(default=0, ge=0),
    page_size: int | None = Query(default=50, ge=0, le=200),
) -> list[dict]:
    params = dict(page_number=page_number, page_size=page_size)
    genres = await genre_service.get_list_genres(params)
    if not genres:
        logger.warning("Was not a single genre")
        return []

    return genres
