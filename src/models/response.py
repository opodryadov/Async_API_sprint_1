from pydantic import BaseModel


class AdditionalResponseModel(BaseModel):
    detail: list[str]


class BadRequest(AdditionalResponseModel):
    pass


class NotFound(AdditionalResponseModel):
    pass
