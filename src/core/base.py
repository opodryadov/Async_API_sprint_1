import os
from logging import config as logging_config

from src.core import logger


logging_config.dictConfig(logger.LOGGING)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROJECT_HOST = os.getenv("PROJECT_HOST", "0.0.0.0")
PROJECT_PORT = int(os.getenv("PROJECT_PORT", 8000))
