from typing import Optional

from elasticsearch import NotFoundError

from src import core
from src.common.connectors.es import ESConnector
from src.common.connectors.redis import RedisConnector
from src.models import Genre


class GenreService:
    def __init__(self):
        self.redis = RedisConnector()
        self.elastic = ESConnector()

    async def get_by_id(self, genre_id: str) -> Optional[Genre]:
        genre = await self._genre_from_cache(genre_id)
        if not genre:
            genre = await self._get_genre_elastic(genre_id)
            if not genre:
                return None
            await self._put_genre_to_cache(genre)

        return genre

    async def _get_genre_elastic(self, genre_id: str) -> Optional[Genre]:
        try:
            doc = await self.elastic.es.get("genres", genre_id)
        except NotFoundError:
            return None
        return Genre(**doc["_source"])

    async def _genre_from_cache(self, genre_id: str) -> Optional[Genre]:
        data = await self.redis.redis.get(genre_id)
        if not data:
            return None

        genre = Genre.parse_raw(data)
        return genre

    async def _put_genre_to_cache(self, genre: Genre):
        await self.redis.redis.set(
            genre.id, genre.json(), core.CACHE_EXPIRE_IN_SECONDS
        )
