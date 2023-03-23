from functools import lru_cache

from aioredis import Redis
from fastapi import Depends

from src.common.connectors.redis import get_redis
from src.common.storages.caches.redis import RedisCacheBase
from src.core import settings
from src.models.search import IndexName


class FilmRedisStorage(RedisCacheBase):
    cache_prefix = IndexName.MOVIES.value
    default_ttl = settings.cache_expire


class GenreRedisStorage(RedisCacheBase):
    cache_prefix = IndexName.GENRES.value
    default_ttl = settings.cache_expire


class PersonRedisStorage(RedisCacheBase):
    cache_prefix = IndexName.PERSONS.value
    default_ttl = settings.cache_expire


@lru_cache()
def get_film_redis_storage(
    redis: Redis = Depends(get_redis),
) -> FilmRedisStorage:
    return FilmRedisStorage(redis)


@lru_cache()
def get_genre_redis_storage(
    redis: Redis = Depends(get_redis),
) -> GenreRedisStorage:
    return GenreRedisStorage(redis)


@lru_cache()
def get_person_redis_storage(
    redis: Redis = Depends(get_redis),
) -> PersonRedisStorage:
    return PersonRedisStorage(redis)
