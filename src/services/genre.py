import logging
from functools import lru_cache

from fastapi import Depends

from src.common.storages.es_storage import (
    EsStorage,
    get_elastic_storage_service,
)
from src.common.storages.redis_storage import (
    RedisStorage,
    get_redis_storage_service,
)
from src.models import Genre


logger = logging.getLogger(__name__)


class GenreService:
    def __init__(self, redis_storage: RedisStorage, es_storage: EsStorage):
        self._redis_storage = redis_storage
        self._es_storage = es_storage

    async def get_genre_by_id(self, genre_id: str) -> dict | None:
        genre = await self._redis_storage.get_from_cache(key=genre_id)
        if genre:
            genre = Genre.parse_raw(genre)
            return genre.dict()

        genre = await self._es_storage.get_genre(genre_id)
        if not genre:
            return None
        await self._redis_storage.put_to_cache(
            key=genre.id, value=genre.json()
        )

        return genre.dict()

    async def get_list_genres(self, params) -> list[dict] | None:
        query = dict(
            index="genres",
            body={"query": {"match_all": {}}},
            params={
                "size": params.get("page_size"),
                "from": params.get("page_number"),
            },
        )
        key = await self._redis_storage.get_key(query)
        genres = await self._redis_storage.get_from_cache(key=key)
        if genres:
            genres_deserialize = await self._redis_storage.deserialize(genres)
            genres = [Genre.parse_raw(genre) for genre in genres_deserialize]
            return [genre.dict() for genre in genres]

        genres = await self._es_storage.get_list_genres(query)
        genres_serialize = await self._redis_storage.serialize(
            [genre.json() for genre in genres]
        )
        await self._redis_storage.put_to_cache(key=key, value=genres_serialize)
        genres = [genre.dict() for genre in genres]
        return genres


@lru_cache()
def get_genre_service(
    redis: RedisStorage = Depends(get_redis_storage_service),
    elastic: EsStorage = Depends(get_elastic_storage_service),
) -> GenreService:
    return GenreService(redis, elastic)
