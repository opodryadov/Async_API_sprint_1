import os


ELASTIC_HOST = os.getenv("ELASTIC_HOST", "es")
ELASTIC_PORT = int(os.getenv("ELASTIC_PORT", 9200))

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
FILM_CACHE_EXPIRE_IN_SECONDS = int(
    os.getenv("FILM_CACHE_EXPIRE_IN_SECONDS", default=60 * 5)
)
CACHE_EXPIRE_IN_SECONDS = int(
    os.getenv("CACHE_EXPIRE_IN_SECONDS", default=60 * 5)
)
