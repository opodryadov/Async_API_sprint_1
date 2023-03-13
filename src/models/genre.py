from src.models.base import IdModelMixin, ORDJSONModelMixin


class Genre(IdModelMixin, ORDJSONModelMixin):
    name: str
