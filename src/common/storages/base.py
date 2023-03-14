import abc
from typing import Any


class BaseCacheStorage:
    @abc.abstractmethod
    async def get_from_cache(self, key: str) -> Any:
        """Получить данные из кэша."""

    @abc.abstractmethod
    async def put_to_cache(self, key: str, value: Any) -> None:
        """Сохранить данные в кэше"""

    async def serialize(self, value) -> str:
        """Сериализация"""
        raise NotImplementedError

    async def deserialize(self, str_value: str):
        """Десериализация"""
        raise NotImplementedError


class BaseDataStorage:
    @abc.abstractmethod
    async def get_by_id(self, *args, **kwargs):
        """Получить документ по id"""
        pass

    @abc.abstractmethod
    async def search(self, *args, **kwargs):
        """Получить документы по параметрам"""
        pass