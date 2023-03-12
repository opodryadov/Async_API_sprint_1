from enum import Enum

from pydantic import Field

from src.models.base import IdModelMixin, ORDJSONModelMixin


class PersonRole(str, Enum):
    DIRECTOR = "director"
    WRITER = "writer"
    ACTOR = "actor"


class PersonFilms(IdModelMixin, ORDJSONModelMixin):
    roles: list[str] | None = Field(default=list())


class Person(IdModelMixin, ORDJSONModelMixin):
    full_name: str
    films: list[PersonFilms] | None = Field(default=list())
