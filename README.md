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

### Тестирование (локально)
- установка зависимостей
```bash
pip3 install poetry==1.2.2
poetry install --no-root && poetry shell
```
- сборка контейнеров
```bash
make up_local_compose
```
- создание .env файла(перед сборкой контейнеров следует удалить этот файл, либо взять значения переменных из файла .env.example)
```bash
cp tests/.env_test_local .env
```
- запуск апи(для запуска заменить значение переменной PROJECT_PORT на любой другой порт кроме 8000 и 8080, например 8010)
```bash
python ./manage.py api
```
- запуск тестов
```bash
pytest
```

###  Тест API
[Swagger](http://127.0.0.1:8080/api/swagger)

