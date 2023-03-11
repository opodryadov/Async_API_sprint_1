import os
from logging import config as logging_config

from src.core import logger


logging_config.dictConfig(logger.LOGGING)

REDIS_HOST = os.getenv("REDIS_HOST", "127.0.0.1")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
FILM_CACHE_EXPIRE_IN_SECONDS = int(
    os.getenv("FILM_CACHE_EXPIRE_IN_SECONDS", default=60 * 5)
)
CACHE_EXPIRE_IN_SECONDS = int(
    os.getenv("CACHE_EXPIRE_IN_SECONDS", default=60 * 5)
)

ELASTIC_HOST = os.getenv("ELASTIC_HOST", "127.0.0.1")
ELASTIC_PORT = int(os.getenv("ELASTIC_PORT", 9200))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 8080))
