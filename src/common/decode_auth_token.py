import logging
from typing import Optional

import jwt
from dotenv import load_dotenv
from fastapi import Cookie

from src.core import CAS_SECURE_KEY, JWT_ALGORITHM, JWT_SECRET


load_dotenv()

logger = logging.getLogger(__name__)


def get_decoded_data(
    token: Optional[str] = Cookie(None, alias=CAS_SECURE_KEY)
) -> Optional[dict]:
    if not token:
        return None

    try:
        decoded_token = jwt.decode(
            token,
            JWT_SECRET,
            algorithms=[JWT_ALGORITHM],
        )
    except (jwt.ExpiredSignatureError, jwt.DecodeError):
        logger.error("Invalid token or expired signature.", exc_info=True)
        return None
    return decoded_token
