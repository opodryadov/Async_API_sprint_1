from typing import Optional

from elasticsearch import NotFoundError

from src.common.connectors.es import ESConnector
from src.common.storages.redis_storage import RedisStorage
from src.models import Genre


class GenreService:
    def __init__(self):
        self._elastic = ESConnector()
        self._redis_storage = RedisStorage()

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

    async def get_list_genre(self) -> Optional[list[dict]]:
        genres = await self._get_list_genres_elastic()
        if not genres:
            return None
        genres = [genre.dict() for genre in genres]
        return genres

    async def _get_list_genres_elastic(self):
        docs = await self._elastic.es.search(
            index="genres", body={"query": {"match_all": {}}}
        )
        return [Genre(**doc["_source"]) for doc in docs["hits"]["hits"]]

    async def _get_genre_elastic(self, genre_id: str) -> Optional[Genre]:
        try:
            doc = await self._elastic.es.get("genres", genre_id)
        except NotFoundError:
            return None
        return Genre(**doc["_source"])
