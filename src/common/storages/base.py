import abc


class BaseDataSearch(abc.ABC):
    @abc.abstractmethod
    async def search_by_id(self, *args, **kwargs):
        """Поиск по id"""

    @abc.abstractmethod
    async def search_by_query(self, *args, **kwargs):
        """Поиск по параметрам"""


class BaseDataStorage(abc.ABC):
    @abc.abstractmethod
    async def get_document_by_id(self, doc_id: str):
        """Получить по id"""

    @abc.abstractmethod
    async def get_list_documents(self, *args, **kwargs):
        """Получить список документов по параметрам"""
