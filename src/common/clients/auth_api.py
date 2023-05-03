from typing import Any, Dict, Optional

from httpx import AsyncClient

from src.common.collections import get_in
from src.core import settings


class AuthApiClient(AsyncClient):
    def __init__(self):
        super().__init__(base_url=settings.auth_api_url)

    @property
    def default_headers(self) -> Dict:
        return {"X-Token": settings.auth_api_srv_token}

    async def get_all_roles_srv(self) -> list[dict]:
        """Получить весь список ролей."""

        url = "/api/srv/roles"
        response_body = await self.get(url=url, headers=self.default_headers)
        resp = response_body.json()
        return get_in(resp, "result")

    async def add_role_to_user_srv(
        self, user_id: str, role_id: str
    ) -> Optional[Dict[str, Any]]:
        """Назначить пользователю роль."""

        url = "/api/srv/roles"
        body = {
            "user_id": user_id,
            "roles": role_id,
        }
        response_body = await self.post(
            url=url, headers=self.default_headers, json=body
        )
        resp = response_body.json()
        return get_in(resp, "result")

    async def delete_role_to_user_srv(
        self, user_id: str, role_id: str
    ) -> Optional[Dict[str, Any]]:
        """Удалить у пользователя роль."""

        url = "/api/srv/roles"
        params = {
            "user_id": user_id,
            "roles": role_id,
        }
        response_body = await self.delete(
            url=url, headers=self.default_headers, params=params
        )
        resp = response_body.json()
        return get_in(resp, "result")

    async def check_permissions_user_srv(
        self, user_id: str
    ) -> Optional[Dict[str, Any]]:
        """Удалить у пользователя роль."""

        url = "/api/srv/roles/check_permissions"
        response_body = await self.get(
            url=url, headers=self.default_headers, params={"user_id": user_id}
        )
        resp = response_body.json()
        return get_in(resp, "result")

    async def create_new_role_srv(
        self, role_name: str, description: str
    ) -> Optional[Dict[str, Any]]:
        """ "Создать роль в бд."""

        url = "/api/srv/roles/create_role"
        body = {
            "role_name": role_name,
            "description": description,
        }
        response_body = await self.post(
            url=url, headers=self.default_headers, json=body
        )
        resp = response_body.json()
        return get_in(resp, "result")

    async def delete_role_srv(self, role_id: str) -> None:
        """Удалить роль из бд."""

        url = f"/api/srv/roles/{role_id}/delete_role"
        response_body = await self.delete(
            url=url, headers=self.default_headers
        )
        return response_body.json()
