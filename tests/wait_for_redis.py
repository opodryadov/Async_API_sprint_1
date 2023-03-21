import logging

import backoff
from functional.core import test_settings
from redis import Redis, exceptions


logger = logging.getLogger(__name__)


@backoff.on_exception(
    backoff.expo,
    (exceptions.ConnectionError,),
    max_tries=10,
)
def ping_redis():
    redis = Redis(
        host=test_settings.redis_host, port=test_settings.redis_port, ssl=False
    )
    if not redis.ping():
        logger.warning("Redis is not ready")
        raise exceptions.ConnectionError("Connect to redis is failed.")
    logger.info("Redis is ready")


if __name__ == "__main__":
    ping_redis()
