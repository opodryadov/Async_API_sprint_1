from pydantic import Field

from src.models.base import IdModelMixin, ORDJSONModelMixin


class Person(IdModelMixin, ORDJSONModelMixin):
    full_name: str
    # role: str
    film_ids: list[str] | None = Field(default=list())
