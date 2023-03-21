from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseModel, BaseSettings, Field


load_dotenv()


class TestSettings(BaseSettings):
    project_host: str = Field(env="PROJECT_HOST", default="fastapi")
    project_port: int = Field(env="PROJECT_PORT", default="8000")

    elastic_host: str = Field(env="ELASTIC_HOST", default="es")
    elastic_port: int = Field(env="ELASTIC_PORT", default=9200)

    redis_host: str = Field(env="REDIS_HOST", default="redis")
    redis_port: int = Field(env="REDIS_PORT", default=6379)

    cache_expire: int = Field(env="CACHE_EXPIRE_IN_SECONDS", default=300)

    log_format: str = Field(env="LOG_FORMAT", default="DEBUG")

    class Config:
        env_file: str = ".env_test"
        env_file_encoding: str = "utf-8"


test_settings = TestSettings()


class ESIndexSettings(BaseModel):
    index_name: str
    schema_file_path: Path
    data_file_path: Path
