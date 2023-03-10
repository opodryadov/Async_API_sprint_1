import logging
from datetime import datetime
from typing import Generator

import psycopg2
from backoff import backoff
from psycopg2.extensions import connection
from query import query


logger = logging.getLogger(__name__)


class PostgresExtractor:
    """
    В этом классе данные, полученные из Postgres, преобразуются во внутренний формат
    """

    @backoff()
    def __init__(self, conn: connection) -> None:
        self.connection = conn

    @backoff()
    def extract(self, last_modified: datetime) -> Generator:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (last_modified,) * 3)
                while data := cursor.fetchmany(200):
                    yield data

        except psycopg2.Error as err:
            logger.error(err)
            return
