import logging

from fastapi import APIRouter, Depends

from src.common.clients.auth_api import AuthApiClient
from src.common.exceptions import BadRequestError, ClientError, ServiceError
from src.models.role import Role


logger = logging.getLogger(__name__)


router = APIRouter()


@router.get(
    "",
    response_model=list[Role],
    summary="Список ролей",
    description="Список ролей",
    response_description="Весь список ролей",
)
async def list_roles(auth_api_client=Depends(AuthApiClient)):
    try:
        roles = await auth_api_client.get_all_roles_srv()
    except (BadRequestError, ServiceError, ClientError):
        logger.warning("Error getting list roles.", exc_info=True)
        return

    return roles
