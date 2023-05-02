from typing import Dict

from httpx import Client

from src.common.collections import get_in


class AuthApiClient(Client):
    def __init__(self, token: str = ""):
        super().__init__()
        self.token = token

    @property
    def default_headers(self) -> Dict:
        return {"X-Token": self.token}

    def get_all_roles_srv(self):
        url = "/api/srv/roles"
        response_body, _ = self.get(url=url, headers=self.default_headers)
        roles = get_in(response_body, "result")
        return roles
