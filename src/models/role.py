import enum
from typing import List

from src.models import ORDJSONModelMixin


class RoleType(str, enum.Enum):
    ROLE_PORTAL_ADMIN = "ROLE_PORTAL_ADMIN"
    ROLE_PORTAL_USER = "ROLE_PORTAL_USER"
    ROLE_SUBSCRIBER = "ROLE_SUBSCRIBER"


class Role(ORDJSONModelMixin):
    role_id: str
    name: str


class UserRoleResponse(ORDJSONModelMixin):
    user_id: str
    roles: List[RoleType] = list()
