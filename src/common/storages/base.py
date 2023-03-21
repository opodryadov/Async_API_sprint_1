import abc


class BaseDataStorage:
    @abc.abstractmethod
    async def get_by_id(self, *args, **kwargs):
        """Получить документ по id"""

    @abc.abstractmethod
    async def search(self, *args, **kwargs):
        """Получить документы по параметрам"""
