from functools import lru_cache

from fastapi import Depends

from src.models import Genre
from src.models.search import IndexName
from src.services.base import Service
from src.services.es_storage import GenreEsStorage, get_genre_elastic_storage
from src.services.redis_storage import (
    GenreRedisStorage,
    get_genre_redis_storage,
)


class GenreService(Service):
    index_name = IndexName.GENRES.value
    detail_model = Genre
    model = Genre


@lru_cache()
def get_genre_service(
    redis: GenreRedisStorage = Depends(get_genre_redis_storage),
    elastic: GenreEsStorage = Depends(get_genre_elastic_storage),
) -> GenreService:
    return GenreService(redis, elastic)
