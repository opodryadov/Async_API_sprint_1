import logging
from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException

from src.common.utils import query_params
from src.models import Genre
from src.models.response import BadRequest, NotFound
from src.services.genre import GenreService


router = APIRouter()

logger = logging.getLogger(__name__)


@router.get(
    "/{genre_id}",
    response_model=Genre,
    responses={404: {"model": NotFound}, 400: {"model": BadRequest}},
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


@router.get("/", response_model=list[Genre])
async def list_genres(
    genre_service: GenreService = Depends(GenreService),
    params: dict = Depends(query_params),
) -> list[dict]:
    genres = await genre_service.get_list_genres(params)
    if not genres:
        logger.warning("Was not a single genre")
        return []

    return genres
