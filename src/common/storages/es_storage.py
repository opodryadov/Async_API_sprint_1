import logging

from elasticsearch import NotFoundError

from src.common.connectors.es import ESConnector
from src.common.storages.base import BaseDataStorage
from src.models import Film, FilmShort, Genre, Person


logger = logging.getLogger(__name__)


class EsStorage(BaseDataStorage):
    def __init__(self):
        self._elastic = ESConnector()

    async def get_by_id(self, index: str, doc_id: str) -> dict | None:
        try:
            doc = await self._elastic.es.get(index=index, id=doc_id)
        except NotFoundError:
            logger.error(
                "Document was not found in ES: doc_id %s index %s",
                doc_id,
                index,
                exc_info=True,
            )
            return None
        return doc["_source"]

    async def search(self, *args, **kwargs) -> dict:
        docs = await self._elastic.es.search(*args, **kwargs)
        return docs["hits"]["hits"]

    async def get_person(self, person_id: str) -> Person | None:
        doc = await self.get_by_id(index="persons", doc_id=person_id)
        if not doc:
            return None
        return Person(**doc)

    async def get_genre(self, genre_id: str) -> Genre | None:
        doc = await self.get_by_id(index="genres", doc_id=genre_id)
        if not doc:
            return None
        return Genre(**doc)

    async def get_film(self, film_id: str) -> Film | None:
        doc = await self.get_by_id(index="movies", doc_id=film_id)
        if not doc:
            return None
        return Film(**doc)

    async def get_list_films(self, query: dict) -> list[Film]:
        docs = await self.search(**query)
        movies = [Film(**doc["_source"]) for doc in docs]
        return movies

    async def get_list_short_films(self, query: dict) -> list[FilmShort]:
        docs = await self.search(**query)
        movies = [FilmShort(**doc["_source"]) for doc in docs]
        return movies

    async def get_list_genres(self, query: dict) -> list[Genre]:
        docs = await self.search(**query)
        genres = [Genre(**doc["_source"]) for doc in docs]
        return genres

    async def get_list_persons(self, query: dict) -> list[Person]:
        docs = await self.search(**query)
        persons = [Person(**doc["_source"]) for doc in docs]
        return persons
