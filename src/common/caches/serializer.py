import abc


class BaseSerializer:
    @abc.abstractmethod
    def serialize(self, value) -> str:
        """Сериализация"""

    @abc.abstractmethod
    def deserialize(self, str_value: str):
        """Десериализация"""
