import abc
from typing import TypeVar

from src.common.storages.caches.redis import RedisCacheBase
from src.common.storages.elastic import EsStorageBase
from src.models.search import IndexName, ModelSearchQuery


BaseModelType = TypeVar("BaseModelType", bound="BaseModel")


class BaseService:
    @abc.abstractmethod
    async def get_by_id(self, item_id: str):
        pass

    @abc.abstractmethod
    async def get_list(self, *args, **kwargs):
        pass


class Service(BaseService):
    index_name: str = None
    model: BaseModelType = None
    detail_model: BaseModelType = None

    def __init__(
        self, redis_storage: RedisCacheBase, es_storage: EsStorageBase
    ):
        self._redis_storage = redis_storage
        self._es_storage = es_storage

    async def get_by_id(self, item_id: str):
        item = await self._redis_storage.get_from_cache(key=item_id)
        if item:
            item = self.detail_model.parse_raw(item)
            return item

        item = await self._es_storage.get_document_by_id(doc_id=item_id)
        if not item:
            return None
        await self._redis_storage.put_to_cache(key=item.id, value=item.json())

        return item

    async def get_list(self, params: dict) -> list[BaseModelType]:
        search_query = self.get_search_query(params)
        key = self._redis_storage.get_key(search_query)
        items = await self._redis_storage.get_from_cache(key=key)
        if items:
            items_deserialize = self._redis_storage.deserialize(items)
            items = [self.model.parse_raw(item) for item in items_deserialize]
            return items

        items = await self._es_storage.get_list_documents(search_query)
        items_serialize = self._redis_storage.serialize(
            [item.json() for item in items]
        )
        await self._redis_storage.put_to_cache(key=key, value=items_serialize)
        return items

    def get_search_query(self, params: dict) -> dict:
        return self._build_search_query(params=params).dict(exclude_none=True)

    def _build_search_query(self, params: dict) -> ModelSearchQuery:
        query = params.get("query")
        sort = params.get("sort")
        genre = params.get("genre")
        search_type = params.get("search_type")
        params = {
            "size": params.get("page_size"),
            "from": params.get("page_number") - 1,
        }
        search_query = ModelSearchQuery()

        search_query.body = {"query": {"match_all": {}}}
        if self.index_name == IndexName.PERSONS.value and query:
            search_query.body = {"query": {"match": {"full_name": query}}}
        if (
            self.index_name == IndexName.MOVIES.value
            and search_type == "search_films"
            and query
        ):
            search_query.body = {
                "query": {
                    "bool": {
                        "must": {
                            "multi_match": {
                                "query": query,
                                "type": "most_fields",
                                "fields": ["title", "description"],
                            }
                        }
                    }
                }
            }
        if (
            self.index_name == IndexName.MOVIES.value
            and search_type == "films_genre"
            and genre
        ):
            search_query.body = {
                "query": {
                    "nested": {
                        "path": "genre",
                        "query": {"match": {"genre.id": genre}},
                    }
                }
            }
        if sort:
            search_query.body.update({"sort": sort})

        search_query.index = self.index_name
        search_query.params = params
        return search_query
