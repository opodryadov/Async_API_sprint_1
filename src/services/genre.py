from functools import lru_cache

from fastapi import Depends

from src.common.storages.caches.redis import RedisCacheBase
from src.models import Genre
from src.models.index import IndexName
from src.services.es_storage import EsStorageBase, get_genre_elastic_storage
from src.services.redis_storage import get_genre_redis_storage


class GenreService:
    def __init__(
        self, redis_storage: RedisCacheBase, es_storage: EsStorageBase
    ):
        self._redis_storage = redis_storage
        self._es_storage = es_storage

    async def get_genre_by_id(self, genre_id: str) -> dict | None:
        genre = await self._redis_storage.get_from_cache(key=genre_id)
        if genre:
            genre = Genre.parse_raw(genre)
            return genre.dict()

        genre = await self._es_storage.get_document_by_id(genre_id)
        if not genre:
            return None
        await self._redis_storage.put_to_cache(
            key=genre.id, value=genre.json()
        )

        return genre.dict()

    async def get_list_genres(self, params) -> list[dict] | None:
        query = dict(
            index=IndexName.GENRES,
            body={"query": {"match_all": {}}},
            params={
                "size": params.get("page_size"),
                "from": params.get("page_number"),
            },
        )
        key = self._redis_storage.get_key(query)
        genres = await self._redis_storage.get_from_cache(key=key)
        if genres:
            genres_deserialize = self._redis_storage.deserialize(genres)
            genres = [Genre.parse_raw(genre) for genre in genres_deserialize]
            return [genre.dict() for genre in genres]

        genres = await self._es_storage.get_list_documents(query)
        genres_serialize = self._redis_storage.serialize(
            [genre.json() for genre in genres]
        )
        await self._redis_storage.put_to_cache(key=key, value=genres_serialize)
        genres = [genre.dict() for genre in genres]
        return genres


@lru_cache()
def get_genre_service(
    redis: RedisCacheBase = Depends(get_genre_redis_storage),
    elastic: EsStorageBase = Depends(get_genre_elastic_storage),
) -> GenreService:
    return GenreService(redis, elastic)
