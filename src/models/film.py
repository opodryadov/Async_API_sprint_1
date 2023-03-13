from pydantic import Field

from src.models.base import IdModelMixin, ORDJSONModelMixin


class FilmPerson(IdModelMixin, ORDJSONModelMixin):
    full_name: str


class FilmGenre(IdModelMixin, ORDJSONModelMixin):
    name: str


class Film(IdModelMixin, ORDJSONModelMixin):
    title: str | None
    imdb_rating: float | None = Field(default=0.0)
    description: str | None = Field(default="")
    genre: list[FilmGenre] | None
    actors: list[FilmPerson] | None
    writers: list[FilmPerson] | None
    directors: list[FilmPerson] | None


class FilmShort(IdModelMixin, ORDJSONModelMixin):
    title: str | None
    imdb_rating: float | None = Field(default=0.0)
