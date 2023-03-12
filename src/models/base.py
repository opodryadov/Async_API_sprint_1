from typing import TypedDict

import orjson
from pydantic import BaseModel, Field


def orjson_dumps(v, *, default):
    return orjson.dumps(v, default=default).decode()


class IdModelMixin(BaseModel):
    id: str = Field(alias="uuid")


class ORDJSONModelMixin(BaseModel):
    class Config:
        allow_population_by_field_name = True
        json_loads = orjson.loads
        json_dumps = orjson_dumps


class NestedModelMixin(TypedDict, total=False):
    id: str
