import logging

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.v1 import films, genres, persons
from core import config
from core.logger import LOGGING
from src.db.elastic import ESConnector
from src.db.redis import RedisConnector


app = FastAPI(
    on_startup=[
        RedisConnector.setup,
        ESConnector.setup,
    ],
    on_shutdown=[
        RedisConnector.close,
        ESConnector.close,
    ],
    title="Read-only API для онлайн-кинотеатра",
    description="Информация о фильмах, жанрах и людях, участвовавших в создании произведения",
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
    version="1.0.0",
)

app.include_router(films.router, prefix="/api/v1/films", tags=["Фильмы"])
app.include_router(persons.router, prefix="/api/v1/persons", tags=["Персоны"])
app.include_router(genres.router, prefix="/api/v1/genres", tags=["Жанры"])

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=config.HOST,
        port=config.PORT,
        log_config=LOGGING,
        log_level=logging.DEBUG,
    )
