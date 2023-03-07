from pydantic import Field

from src.models.base import ModelMixin


class Genre(ModelMixin):
    name: str
    description: str | None = Field(default="")
