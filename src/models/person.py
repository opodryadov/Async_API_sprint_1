from enum import Enum

from pydantic import Field

from src.models.base import IdModelMixin, ORDJSONModelMixin


class PersonRole(str, Enum):
    DIRECTOR = "director"
    WRITER = "writer"
    ACTOR = "actor"


class NestedPersonFilm(IdModelMixin, ORDJSONModelMixin):
    roles: list[str] | None


class Person(IdModelMixin, ORDJSONModelMixin):
    full_name: str
    films: list[NestedPersonFilm] | None


class PersonFilm(IdModelMixin, ORDJSONModelMixin):
    title: str | None
    imdb_rating: float | None = Field(default=0.0)
