from datetime import datetime
from pydantic import Field
from src.models.base import ModelMixin, NestedModelMixin


class FilmPerson(NestedModelMixin):
    full_name: str


class FilmGenre(NestedModelMixin):
    name: str


class Film(ModelMixin):
    title: str
    imdb_rating: float | None = Field(default=0.0)
    description: str | None = Field(default="")
    genre: list[FilmGenre] | None = Field(default=list())
    actors: list[FilmPerson] | None = Field(default=list())
    writers: list[FilmPerson] | None = Field(default=list())
    directors: list[FilmPerson] | None = Field(default=list())
    creation_date: datetime | None = Field(default=None)
    age_limit: int | None = Field(default=None)
    file_path: str | None = Field(default=None)
