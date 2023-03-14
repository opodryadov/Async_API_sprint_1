import logging
from typing import Optional

from elasticsearch import NotFoundError

from src.common.storages.es_storage import EsStorage
from src.common.storages.redis_storage import RedisStorage
from src.models import Genre


logger = logging.getLogger(__name__)


class GenreService:
    def __init__(self):
        self._redis_storage = RedisStorage()
        self._es_storage = EsStorage()

    async def get_genre_by_id(self, genre_id: str) -> Optional[dict]:
        genre = await self._redis_storage.get_from_cache(key=genre_id)
        if genre:
            genre = Genre.parse_raw(genre)
            return genre.dict()

        genre = await self._get_genre_elastic(genre_id)
        if not genre:
            return None
        await self._redis_storage.put_to_cache(
            key=genre.id, value=genre.json()
        )

        return genre.dict()

    async def get_list_genre(self, params) -> Optional[list[dict]]:
        genres = await self._get_list_genres_elastic(params)
        if not genres:
            return None
        genres = [genre.dict() for genre in genres]
        return genres

    async def _get_list_genres_elastic(self, params):
        query = dict(
            index="genres",
            body={"query": {"match_all": {}}},
            params={
                "size": params.get("page_size"),
                "from": params.get("page_number") - 1,
            },
        )
        key = await self._redis_storage.get_key(query)
        genres = await self._redis_storage.get_from_cache(key=key)
        if genres:
            genres_deserialize = await self._redis_storage.deserialize(genres)
            genres = [Genre.parse_raw(genre) for genre in genres_deserialize]
            return genres

        docs = await self._es_storage.search(**query)
        genres = [Genre(**doc["_source"]) for doc in docs]
        genres_serialize = await self._redis_storage.serialize(
            [genre.json() for genre in genres]
        )
        await self._redis_storage.put_to_cache(key=key, value=genres_serialize)
        return genres

    async def _get_genre_elastic(self, genre_id: str) -> Optional[Genre]:
        try:
            doc = await self._es_storage.get_by_id(
                index="genres", doc_id=genre_id
            )
        except NotFoundError:
            logger.error("Genre was not found in ES: %s", genre_id)
            return None
        return Genre(**doc)
