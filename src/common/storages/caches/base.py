import abc
from typing import Any


class BaseCache(abc.ABC):
    @abc.abstractmethod
    async def get_from_cache(self, key: str) -> Any:
        """Получить данные из кэша."""

    @abc.abstractmethod
    async def put_to_cache(self, key: str, value: Any) -> None:
        """Сохранить данные в кэше"""
