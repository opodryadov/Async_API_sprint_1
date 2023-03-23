from enum import Enum
from typing import Optional

from src.models import ORDJSONModelMixin


class IndexName(str, Enum):
    MOVIES = "movies"
    GENRES = "genres"
    PERSONS = "persons"


class ModelSearchQuery(ORDJSONModelMixin):
    index: Optional[str]
    body: Optional[dict]
    params: Optional[dict]
