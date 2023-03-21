import logging
from functools import lru_cache
from typing import Optional

from fastapi import Depends

from src.common.storages.es_storage import (
    EsStorage,
    get_elastic_storage_service,
)
from src.common.storages.redis_storage import (
    RedisStorage,
    get_redis_storage_service,
)
from src.models import Film, FilmShort


logger = logging.getLogger(__name__)


class FilmService:
    def __init__(self, redis_storage: RedisStorage, es_storage: EsStorage):
        self._redis_storage = redis_storage
        self._es_storage = es_storage

    async def get_film_by_id(self, film_id: str) -> Optional[Film]:
        film = await self._redis_storage.get_from_cache(key=film_id)
        if film:
            film = Film.parse_raw(film)
            return film

        film = await self._es_storage.get_film(film_id)
        if not film:
            return None
        await self._redis_storage.put_to_cache(key=film.id, value=film.json())

        return film

    async def get_all_films(
        self, params: dict, genre: str
    ) -> Optional[list[FilmShort]]:
        films = await self._get_films_genre_sort(params, genre)
        if not films:
            return None

        return films

    async def search_films(self, params: dict) -> Optional[list[FilmShort]]:
        films = await self._search_films(params)
        if not films:
            return None

        return films

    async def _get_films_genre_sort(
        self, params: dict, genre: str
    ) -> Optional[list[FilmShort]]:
        query = dict(
            index="movies",
            body={
                "from": params.get("page_number"),
                "size": params.get("page_size"),
                "query": {"match_all": {}}
                if not params.get("genre")
                else {
                    "nested": {
                        "path": "genre",
                        "query": {"match": {"genre.id": genre}},
                    }
                },
                "sort": params.get("sort"),
            },
        )
        key = await self._redis_storage.get_key(query)
        short_films = await self._redis_storage.get_from_cache(key=key)
        if short_films:
            films_deserialize = await self._redis_storage.deserialize(
                short_films
            )
            short_films = [
                FilmShort.parse_raw(film) for film in films_deserialize
            ]
            return short_films

        short_films = await self._es_storage.get_list_short_films(query)
        films_serialize = await self._redis_storage.serialize(
            [film.json() for film in short_films]
        )
        await self._redis_storage.put_to_cache(key=key, value=films_serialize)
        return short_films

    async def _search_films(self, params: dict):
        query = dict(
            index="movies",
            body={
                "from": params.get("page_number"),
                "size": params.get("page_size"),
                "query": {
                    "bool": {
                        "must": {
                            "multi_match": {
                                "query": params.get("query"),
                                "type": "most_fields",
                                "fields": ["title", "description"],
                            }
                        }
                    }
                },
                "sort": params.get("sort"),
            },
        )
        key = await self._redis_storage.get_key(query)
        short_films = await self._redis_storage.get_from_cache(key=key)
        if short_films:
            films_deserialize = await self._redis_storage.deserialize(
                short_films
            )
            short_films = [
                FilmShort.parse_raw(film) for film in films_deserialize
            ]
            return short_films

        short_films = await self._es_storage.get_list_short_films(query)
        films_serialize = await self._redis_storage.serialize(
            [film.json() for film in short_films]
        )
        await self._redis_storage.put_to_cache(key=key, value=films_serialize)
        return short_films


@lru_cache()
def get_film_service(
    redis: RedisStorage = Depends(get_redis_storage_service),
    elastic: EsStorage = Depends(get_elastic_storage_service),
) -> FilmService:
    return FilmService(redis, elastic)
