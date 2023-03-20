import datetime
import json
import uuid
from http import HTTPStatus

import pytest

from tests.functional.core import test_settings


pytestmark = pytest.mark.asyncio

#  Название теста должно начинаться со слова `test_`
#  Любой тест с асинхронными вызовами нужно оборачивать декоратором `pytest.mark.asyncio`, который следит за запуском и работой цикла событий.
async def test_search(es_client, test_client, flush_indexes):
    # 1. Генерируем данные для ES
    es_data = [
        {
            "id": str(uuid.uuid4()),
            "imdb_rating": 8.5,
            "genre": ["Action", "Sci-Fi"],
            "title": "The Star",
            "description": "New World",
            "director": ["Stan"],
            "actors_names": ["Ann", "Bob"],
            "writers_names": ["Ben", "Howard"],
            "actors": [
                {"id": "111", "name": "Ann"},
                {"id": "222", "name": "Bob"},
            ],
            "writers": [
                {"id": "333", "name": "Ben"},
                {"id": "444", "name": "Howard"},
            ],
            "created_at": datetime.datetime.now().isoformat(),
            "updated_at": datetime.datetime.now().isoformat(),
            "film_work_type": "movie",
        }
        for _ in range(60)
    ]

    bulk_query = []
    for row in es_data:
        bulk_query.extend(
            [
                json.dumps(
                    {
                        "index": {
                            "_index": test_settings.es_index,
                            "_id": row[test_settings.es_id_field],
                        }
                    }
                ),
                json.dumps(row),
            ]
        )

    str_query = "\n".join(bulk_query) + "\n"
    # es_client = Elasticsearch(
    #     hosts=f"http://{test_settings.elastic_host}:{test_settings.elastic_port}",
    #     validate_cert=False,
    #     use_ssl=False,
    # )
    # print("--ping2", await es_client.ping(), "host", test_settings.elastic_host, "port", test_settings.elastic_port)
    #
    # # 2. Загружаем данные в ES
    response = await es_client.bulk(str_query, refresh=True)
    if response["errors"]:
        raise Exception("Ошибка записи данных в Elasticsearch")

    # 3. Запрашиваем данные из ES по API
    query_data = {"query": "The Star"}
    response = await test_client.get("/api/v1/films/search", params=query_data)

    assert response.status_code == HTTPStatus.OK
    assert len(response.json()) == 50
