from functools import lru_cache
from typing import Optional

from fastapi import Depends

from src.common.storages.caches.redis import RedisCacheBase
from src.models import Film, FilmShort
from src.models.search import IndexName
from src.services.base import Service
from src.services.es_storage import EsStorageBase, get_film_elastic_storage
from src.services.redis_storage import get_film_redis_storage


class FilmService(Service):
    index_name = IndexName.MOVIES.value
    detail_model = Film
    model = FilmShort

    async def get_all_films(self, params: dict) -> Optional[list[FilmShort]]:
        params.update({"search_type": "films_genre"})
        films = await self.get_list(params)
        if not films:
            return None

        return films

    async def search_films(self, params: dict) -> Optional[list[FilmShort]]:
        params.update({"search_type": "search_films"})
        films = await self.get_list(params)
        if not films:
            return None

        return films


@lru_cache()
def get_film_service(
    redis: RedisCacheBase = Depends(get_film_redis_storage),
    elastic: EsStorageBase = Depends(get_film_elastic_storage),
) -> FilmService:
    return FilmService(redis, elastic)
