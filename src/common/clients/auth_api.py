from typing import Dict

from httpx import AsyncClient

from src.common.collections import get_in
from src.core import settings


class AuthApiClient(AsyncClient):
    def __init__(self):
        super().__init__(base_url=settings.auth_api_url)

    @property
    def default_headers(self) -> Dict:
        return {"X-Token": settings.auth_api_srv_token}

    async def get_all_roles_srv(self):
        url = "/api/srv/roles"
        response_body = await self.get(url=url, headers=self.default_headers)
        resp = response_body.json()
        roles = get_in(resp, "result")
        return roles
