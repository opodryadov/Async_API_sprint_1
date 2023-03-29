import logging


logging.basicConfig(
    format="[%(asctime)s] %(levelname)-8s [LINE:%(lineno)d]: %(message)s",
    level="INFO",
)
logger = logging.getLogger(__name__)


def backoff_handler(details):
    logger.error("Backing off {wait:0.1f} seconds after {tries} tries "
                 "calling function {target} with args {args} and kwargs "
                 "{kwargs}".format(**details))
