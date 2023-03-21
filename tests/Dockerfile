FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH ./src

WORKDIR /code

RUN pip install -U pip==22.0.4 --no-cache-dir && pip install poetry==1.2.2 --no-cache-dir

COPY .. .

RUN poetry config virtualenvs.create false && poetry install --no-root
