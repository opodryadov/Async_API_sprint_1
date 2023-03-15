from pydantic import BaseSettings
from pydantic.fields import Field
from dotenv import load_dotenv


load_dotenv()


class Settings(BaseSettings):
    elastic_host: str = Field(env="ELASTIC_HOST", default="es")
    elastic_port: int = Field(env="ELASTIC_PORT", default=9200)

    redis_host: str = Field(env="REDIS_HOST", default="redis")
    redis_port: int = Field(env="REDIS_PORT", default=6379)

    cache_expire: int = Field(env="CACHE_EXPIRE_IN_SECONDS", default=300)

    log_format: str = Field(env="LOG_FORMAT", default="INFO")

    class Config:
        env_file: str = ".env"
        env_file_encoding: str = "utf-8"


settings = Settings()
