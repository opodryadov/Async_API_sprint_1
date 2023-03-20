import logging

import backoff
from elasticsearch import ConnectionError, Elasticsearch
from functional.core import test_settings


logger = logging.getLogger(__name__)


@backoff.on_exception(
    backoff.expo,
    (ConnectionError,),
    max_tries=10,
)
def ping_es():
    es_client = Elasticsearch(
        hosts=f"http://{test_settings.elastic_host}:{test_settings.elastic_port}",
        validate_cert=False,
        use_ssl=False,
    )
    if not es_client.ping():
        logger.warning("ES is not ready")
        raise ConnectionError("Connect to ES is failed.")
    logger.info("ES is ready")


if __name__ == "__main__":
    ping_es()
