import enum

from pydantic import BaseModel


class RoleType(str, enum.Enum):
    ROLE_PORTAL_ADMIN = "ROLE_PORTAL_ADMIN"
    ROLE_PORTAL_USER = "ROLE_PORTAL_USER"
    ROLE_SUBSCRIBER = "ROLE_SUBSCRIBER"


class Role(BaseModel):
    role_id: str
    name: str
