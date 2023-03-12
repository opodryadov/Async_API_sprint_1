from enum import Enum

from pydantic import Field

from src.models.base import IdModelMixin, ORDJSONModelMixin


class PersonRole(str, Enum):
    DIRECTOR = "director"
    WRITER = "writer"
    ACTOR = "actor"


class Person(IdModelMixin, ORDJSONModelMixin):
    full_name: str
    role: str | None = Field(default="")
    film_ids: list[str] | None = Field(default=list())
