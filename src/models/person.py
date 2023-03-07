from pydantic import Field

from src.models.base import ModelMixin


class Person(ModelMixin):
    full_name: str
    role: str
    film_ids: list[str] | None = Field(default=list())
