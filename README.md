## Async API

##  Обратите внимание
Доработанный ETL располагается в ветке [**etl**](https://github.com/opodryadov/Async_API_sprint_1/tree/etl) данного репозитория!


###  Сборка и запуск в контейнере
- prod
```bash
make up
```
- local
```bash
make up_local_compose
```

### Тестирование
- установка зависимостей
```bash
pip3 install poetry==1.2.2
poetry install --no-root && poetry shell
```
- создание .env_test файла
```bash
cp .env_test_local .env_test
```
- запуск апи
```bash
python .\manage.py api
```
- запуск тестов
```bash
pytest
```

###  Тест API
[Swagger](http://127.0.0.1:8000/api/swagger)

