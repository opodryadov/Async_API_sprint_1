from typing import TypedDict

import orjson
from pydantic import BaseModel


def orjson_dumps(v, *, default):
    return orjson.dumps(v, default=default).decode()


class ModelMixin(BaseModel):
    uuid: str

    class Config:
        json_loads = orjson.loads
        json_dumps = orjson.dumps


class NestedModelMixin(TypedDict, total=False):
    uuid: str
