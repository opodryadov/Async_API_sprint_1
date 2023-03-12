from typing import TypedDict

import orjson
from pydantic import BaseModel, Field


def orjson_dumps(v, *, default):
    return orjson.dumps(v, default=default).decode()


class IdModelMixin(BaseModel):
    uuid: str = Field(alias="id")


class ORDJSONModelMixin(BaseModel):
    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps


class NestedModelMixin(TypedDict, total=False):
    id: str
