import abc
from typing import Any


class BaseCacheStorage:
    @abc.abstractmethod
    async def get_from_cache(self, key: str) -> Any:
        """Получить данные из кэша."""

    @abc.abstractmethod
    async def put_to_cache(self, key: str, value: Any) -> None:
        """Сохранить данные в кэше"""

    @abc.abstractmethod
    async def serialize(self, value) -> str:
        """Сериализация"""

    @abc.abstractmethod
    async def deserialize(self, str_value: str):
        """Десериализация"""


class BaseDataStorage:
    @abc.abstractmethod
    async def get_by_id(self, *args, **kwargs):
        """Получить документ по id"""

    @abc.abstractmethod
    async def search(self, *args, **kwargs):
        """Получить документы по параметрам"""
