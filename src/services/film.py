import logging
from typing import Optional

from elasticsearch import NotFoundError

from src.common.storages.es_storage import EsStorage
from src.common.storages.redis_storage import RedisStorage
from src.models import Film, FilmShort


logger = logging.getLogger(__name__)


class FilmService:
    def __init__(self):
        self._redis_storage = RedisStorage()
        self._es_storage = EsStorage()

    async def get_film_by_id(self, film_id: str) -> Optional[Film]:
        film = await self._redis_storage.get_from_cache(key=film_id)
        if film:
            film = Film.parse_raw(film)
            return film.dict()

        film = await self._get_film_from_elastic(film_id)
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

    async def _get_film_from_elastic(self, film_id: str) -> Optional[Film]:
        try:
            doc = await self._es_storage.get_by_id(
                index="movies", doc_id=film_id
            )
        except NotFoundError:
            logger.error("Film was not found in ES: %s", film_id)
            return None
        return Film(**doc)

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
        films = await self._redis_storage.get_from_cache(key=key)
        if films:
            films_deserialize = await self._redis_storage.deserialize(films)
            films = [FilmShort.parse_raw(film) for film in films_deserialize]
            return films

        docs = await self._es_storage.search(**query)
        films = [FilmShort(**doc["_source"]) for doc in docs]
        films_serialize = await self._redis_storage.serialize(
            [film.json() for film in films]
        )
        await self._redis_storage.put_to_cache(key=key, value=films_serialize)
        return films

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
        films = await self._redis_storage.get_from_cache(key=key)
        if films:
            films_deserialize = await self._redis_storage.deserialize(films)
            films = [FilmShort.parse_raw(film) for film in films_deserialize]
            return films

        docs = await self._es_storage.search(**query)
        films = [FilmShort(**doc["_source"]) for doc in docs]
        films_serialize = await self._redis_storage.serialize(
            [film.json() for film in films]
        )
        await self._redis_storage.put_to_cache(key=key, value=films_serialize)
        return films
