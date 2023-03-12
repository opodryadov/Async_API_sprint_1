from pydantic import Field

from src.models.base import IdModelMixin, NestedModelMixin, ORDJSONModelMixin


class FilmPerson(NestedModelMixin):
    full_name: str


class FilmGenre(NestedModelMixin):
    name: str


class Film(IdModelMixin, ORDJSONModelMixin):
    title: str | None
    imdb_rating: float | None = Field(default=0.0)
    description: str | None = Field(default="")
    genre: list[FilmGenre] | None = Field(default=list())
    actors: list[FilmPerson] | None = Field(default=list())
    writers: list[FilmPerson] | None = Field(default=list())
    directors: list[FilmPerson] | None = Field(default=list())
