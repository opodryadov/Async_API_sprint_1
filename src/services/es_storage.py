from functools import lru_cache

from elasticsearch import AsyncElasticsearch
from fastapi import Depends

from src.common.connectors.elastic import get_elastic
from src.common.storages.elastic import EsStorageBase
from src.models import Film, FilmShort, Genre, Person
from src.models.search import IndexName


class FilmEsStorage(EsStorageBase):
    index_name = IndexName.MOVIES.value
    model = FilmShort
    detail_model = Film


class GenreEsStorage(EsStorageBase):
    index_name = IndexName.GENRES.value
    model = Genre
    detail_model = Genre


class PersonEsStorage(EsStorageBase):
    index_name = IndexName.PERSONS.value
    model = Person
    detail_model = Person

    async def get_films_by_role(self, person_id: str, role: str) -> list[Film]:
        query = dict(
            index=IndexName.MOVIES.value,
            body={
                "query": {
                    "nested": {
                        "path": role,
                        "query": {"match": {f"{role}.id": f"{person_id}"}},
                    }
                }
            },
        )
        docs = await self.search_by_query(**query)
        movies = [Film(**doc["_source"]) for doc in docs]
        return movies


@lru_cache()
def get_person_elastic_storage(
    elastic: AsyncElasticsearch = Depends(get_elastic),
) -> PersonEsStorage:
    return PersonEsStorage(elastic)


@lru_cache()
def get_film_elastic_storage(
    elastic: AsyncElasticsearch = Depends(get_elastic),
) -> FilmEsStorage:
    return FilmEsStorage(elastic)


@lru_cache()
def get_genre_elastic_storage(
    elastic: AsyncElasticsearch = Depends(get_elastic),
) -> GenreEsStorage:
    return GenreEsStorage(elastic)
