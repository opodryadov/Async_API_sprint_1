from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException

from src.models import Genre
from src.services.genre import GenreService


router = APIRouter()


@router.get("/{genre_id}", response_model=Genre)
async def genre_details(
    genre_id: str,
    genre_service: GenreService = Depends(GenreService),
) -> dict:
    genre = await genre_service.get_genre_by_id(genre_id)
    if not genre:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Genre not found"
        )

    return genre


@router.get("/", response_model=list[Genre])
async def list_genres(
    genre_service: GenreService = Depends(GenreService),
) -> list[dict]:
    genres = await genre_service.get_list_genre()
    if not genres:
        return []

    return genres
