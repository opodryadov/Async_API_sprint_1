import logging

from src.common.connectors.es import ESConnector
from src.common.storages.base import BaseDataStorage


logger = logging.getLogger(__name__)


class EsStorage(BaseDataStorage):
    def __init__(self):
        self._elastic = ESConnector()

    async def get_by_id(self, index: str, doc_id: str):
        try:
            doc = await self._elastic.es.get(index=index, id=doc_id)
        except Exception:
            logger.error(
                "Failed to get the document in ES: doc_id %s index %s",
                doc_id,
                index,
                exc_info=True,
            )
            return None
        return doc["_source"]

    async def search(self, *args, **kwargs):
        docs = await self._elastic.es.search(*args, **kwargs)
        return docs["hits"]["hits"]
