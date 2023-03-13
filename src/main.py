from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from src.api.v1 import films, genres, persons
from src.common.connectors.es import ESConnector
from src.common.connectors.redis import RedisConnector


def create_app() -> FastAPI:
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
        docs_url="/swagger",
        openapi_url="/api/openapi.json",
        default_response_class=ORJSONResponse,
        version="1.0.0",
    )

    app.include_router(films.router, prefix="/api/v1/films", tags=["Фильмы"])
    app.include_router(
        persons.router, prefix="/api/v1/persons", tags=["Персоны"]
    )
    app.include_router(genres.router, prefix="/api/v1/genres", tags=["Жанры"])

    return app
