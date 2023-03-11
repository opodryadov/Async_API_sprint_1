from fastapi import APIRouter, Depends, Request

from src.services.genre import GenreService


router = APIRouter()


@router.get("/{genre_id}")
async def genre_details(
    request: Request,
    genre_id: str,
    genre_service: GenreService = Depends(GenreService),
):
    pass


@router.get("/")
async def list_genres(
    request: Request, genre_service: GenreService = Depends(GenreService)
):
    pass
