import datetime
import logging
import os
import time

import psycopg2
from classes import DataTransform, ElasticsearchLoader, PostgresExtractor
from dotenv import load_dotenv
from psycopg2.extras import DictCursor
from queries import GET_FILM_WORKS_QUERY, GET_PERSONS_QUERY
from storage import JsonFileStorage, State


logger = logging.getLogger("etl")

load_dotenv()

DSL = {
    "dbname": os.environ.get("DB_NAME"),
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASS"),
    "host": os.environ.get("DB_HOST", "127.0.0.1"),
    "port": os.environ.get("DB_PORT", 5432),
    "options": "-c search_path=content",
}


if __name__ == "__main__":
    while True:
        with psycopg2.connect(**DSL, cursor_factory=DictCursor) as conn:
            storage = JsonFileStorage(os.environ.get("FILE_PATH"))
            state = State(storage)

            last_modified = state.get_state("modified")
            if last_modified is None:
                last_modified = datetime.date(1, 1, 1).isoformat()

            TABLES = (
                ("movies", GET_FILM_WORKS_QUERY, (last_modified,) * 3),
                ("persons", GET_PERSONS_QUERY, (last_modified,)),
            )

            extractor = PostgresExtractor(conn)
            transformer = DataTransform()
            loader = ElasticsearchLoader(host=os.environ.get("ES_HOST"))

            for index, query, clause in TABLES:
                film_works = extractor.extract(query, clause)
                for film_work in film_works:
                    data = transformer.transform(index, film_work)
                    loader.load(index, data)
                    state.set_state(
                        "modified", datetime.datetime.now().isoformat()
                    )

                    logger.info("The new row loaded: %s", data)

        conn.close()
        time.sleep(float(os.environ.get("INTERVAL")))
