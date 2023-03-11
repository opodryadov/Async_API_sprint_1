from src.models.base import IdModelMixin, ORDJSONModelMixin


class Person(IdModelMixin, ORDJSONModelMixin):
    full_name: str
