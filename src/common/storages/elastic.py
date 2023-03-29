import logging
from typing import TypeVar

import backoff
from elasticsearch import (
    AsyncElasticsearch,
    ConnectionError,
    ConnectionTimeout,
    NotFoundError,
)

from src.common.handlers import backoff_handler
from src.common.storages.base import BaseDataSearch, BaseDataStorage


logger = logging.getLogger(__name__)

BaseModelType = TypeVar("BaseModelType", bound="BaseModel")


class EsStorageBase(BaseDataSearch, BaseDataStorage):
    index_name: str = None
    model: BaseModelType = None
    detail_model: BaseModelType = None

    def __init__(self, elastic: AsyncElasticsearch):
        self._elastic = elastic

    @backoff.on_exception(
        backoff.expo,
        (
            ConnectionError,
            ConnectionTimeout,
        ),
        max_tries=10,
        max_time=60,
        on_backoff=backoff_handler,
    )
    async def search_by_id(self, index: str, doc_id: str) -> dict | None:
        try:
            doc = await self._elastic.get(index=index, id=doc_id)
        except NotFoundError:
            logger.error(
                "Document was not found in ES: doc_id %s index %s",
                doc_id,
                index,
                exc_info=True,
            )
            return None
        return doc["_source"]

    @backoff.on_exception(
        backoff.expo,
        (
            ConnectionError,
            ConnectionTimeout,
        ),
        max_tries=10,
        max_time=60,
        on_backoff=backoff_handler,
    )
    async def search_by_query(self, *args, **kwargs) -> dict:
        docs = await self._elastic.search(*args, **kwargs)
        return docs["hits"]["hits"]

    async def get_document_by_id(self, doc_id: str) -> BaseModelType | None:
        doc = await self.search_by_id(index=self.index_name, doc_id=doc_id)
        if not doc:
            return None
        return self.detail_model(**doc)

    async def get_list_documents(self, query: dict) -> list[BaseModelType]:
        documents = await self.search_by_query(**query)
        docs = [self.model(**doc["_source"]) for doc in documents]
        return docs
