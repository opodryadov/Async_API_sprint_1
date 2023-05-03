from fastapi import APIRouter, Depends

from src.common.clients.auth_api import AuthApiClient
from src.models.role import Role


router = APIRouter()


@router.get(
    "",
    response_model=list[Role],
    summary="Список ролей",
    description="Список ролей",
    response_description="Весь список ролей",
)
async def list_roles(auth_api_client=Depends(AuthApiClient)) -> list[dict]:
    roles = await auth_api_client.get_all_roles_srv()

    return roles
