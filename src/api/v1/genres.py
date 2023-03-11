from fastapi import APIRouter, Depends, Request

from src.services.genre import GenreService, get_genre_service


router = APIRouter()


@router.get("/{genre_id}")
async def genre_details(
    request: Request,
    genre_id: str,
    genre_service: GenreService = Depends(get_genre_service),
):
    pass


@router.get("/")
async def list_genres(
    request: Request, genre_service: GenreService = Depends(get_genre_service)
):
    pass
