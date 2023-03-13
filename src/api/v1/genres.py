from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException, Request

from src.models import Genre
from src.services.genre import GenreService


router = APIRouter()


@router.get("/{genre_id}", response_model=Genre)
async def genre_details(
    genre_id: str,
    genre_service: GenreService = Depends(GenreService),
):
    genre = await genre_service.get_by_id(genre_id)
    if not genre:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Person not found"
        )

    return Genre(**genre.dict())


@router.get("/")
async def list_genres(
    request: Request, genre_service: GenreService = Depends(GenreService)
):
    pass
