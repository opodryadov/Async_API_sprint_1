from typing import Optional

from elasticsearch import NotFoundError

from src import core
from src.common.connectors.es import ESConnector
from src.common.connectors.redis import RedisConnector
from src.models import Film, FilmShort


class FilmService:
    def __init__(self):
        self._redis = RedisConnector()
        self._elastic = ESConnector()

    async def get_by_id(self, film_id: str) -> Optional[Film]:
        film = await self._film_from_cache(film_id)
        if not film:
            film = await self._get_film_from_elastic(film_id)
            if not film:
                return None
            await self._put_film_to_cache(film)

        return film

    async def get_all_films(self, params: dict, genre: str) -> Optional[list[FilmShort]]:
        films = await self._get_films_genre_sort(params, genre)
        if not films:
            return None

        return films

    async def search_films(self, params: dict) -> Optional[list[FilmShort]]:
        films = await self._search_films(params)
        if not films:
            return None

        return films

    async def _get_film_from_elastic(self, film_id: str) -> Optional[Film]:
        try:
            doc = await self._elastic.es.get("movies", film_id)
        except NotFoundError:
            return None
        return Film(**doc["_source"])

    async def _film_from_cache(self, film_id: str) -> Optional[Film]:
        data = await self._redis.redis.get(film_id)
        if not data:
            return None

        film = Film.parse_raw(data)
        return film

    async def _put_film_to_cache(self, film: Film):
        await self._redis.redis.set(
            film.id, film.json(), core.FILM_CACHE_EXPIRE_IN_SECONDS
        )

    async def _get_films_genre_sort(
        self, params: dict,
        genre: str
    ) -> Optional[list[FilmShort]]:
        body = {
            "from": params.get("page_number"),
            "size": params.get("page_size"),
            "query": {
                "match_all": {}
            } if not params.get("genre") else {
                "nested": {
                    "path": "genre",
                    "query": {
                        "match": {
                            "genre.id": genre
                        }
                    },
                }
            },
            "sort": params.get("sort")
        }
        docs = await self._elastic.es.search(index="movies", body=body)
        return [FilmShort(**doc["_source"]) for doc in docs["hits"]["hits"]]

    async def _search_films(self, params: dict):
        body = {
            "from": params.get("page_number"),
            "size": params.get("page_size"),
            "query": {
                "bool": {
                    "must": {
                        "multi_match": {
                            "query": params.get("query"),
                            "type": "most_fields",
                            "fields": ["title", "description"]
                        }
                    }
                }
            },
            "sort": params.get("sort")
        }
        docs = await self._elastic.es.search(index="movies", body=body)
        return [FilmShort(**doc["_source"]) for doc in docs["hits"]["hits"]]
