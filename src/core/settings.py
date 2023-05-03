from dotenv import load_dotenv
from pydantic import BaseSettings
from pydantic.fields import Field


load_dotenv()


class Settings(BaseSettings):
    project_host: str = Field(env="PROJECT_HOST", default="0.0.0.0")
    project_port: int = Field(env="PROJECT_PORT", default="8000")

    elastic_host: str = Field(env="ELASTIC_HOST", default="es")
    elastic_port: int = Field(env="ELASTIC_PORT", default=9200)

    redis_host: str = Field(env="REDIS_HOST", default="redis")
    redis_port: int = Field(env="REDIS_PORT", default=6379)

    cache_expire: int = Field(env="CACHE_EXPIRE_IN_SECONDS", default=300)

    log_format: str = Field(env="LOG_FORMAT", default="INFO")

    auth_api_srv_token: str = Field(env="AUTH_API_SRV_TOKEN", default="test")
    auth_api_url: str = Field(
        env="AUTH_API_URL", default="http://0.0.0.0:8000"
    )

    class Config:
        env_file: str = ".env"
        env_file_encoding: str = "utf-8"


settings = Settings()
