import os
from pathlib import Path, PurePath

from src.models.index import IndexName
from tests.functional.core.settings import ESIndexSettings


dir_path = os.path.dirname(os.path.realpath(__file__))


film_index = ESIndexSettings(
    index_name=IndexName.MOVIES,
    schema_file_path=Path(PurePath(dir_path, "es_schema_movies.json")),
    data_file_path=Path(PurePath(dir_path, "es_data_movies.json")),
)

genre_index = ESIndexSettings(
    index_name=IndexName.GENRES,
    schema_file_path=Path(PurePath(dir_path, "es_schema_genres.json")),
    data_file_path=Path(PurePath(dir_path, "es_data_genres.json")),
)

person_index = ESIndexSettings(
    index_name=IndexName.PERSONS,
    schema_file_path=Path(PurePath(dir_path, "es_schema_persons.json")),
    data_file_path=Path(PurePath(dir_path, "es_data_persons.json")),
)

INDEXES = [
    film_index,
    genre_index,
    person_index,
]
