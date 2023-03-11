from typing import TypedDict

import orjson
from pydantic import BaseModel


def orjson_dumps(v, *, default):
    return orjson.dumps(v, default=default).decode()


class IdModelMixin(BaseModel):
    id: str


class ORDJSONModelMixin(BaseModel):
    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps


class NestedModelMixin(TypedDict, total=False):
    id: str
