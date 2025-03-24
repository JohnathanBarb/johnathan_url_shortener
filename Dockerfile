FROM python:3.13-alpine

WORKDIR /app

RUN apk add build-base libpq libpq-dev

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY ./johnathan_url_shortener ./johnathan_url_shortener

CMD ["poetry", "run", "uvicorn", "johnathan_url_shortener.main:app", "--host", "0.0.0.0", "--port", "8000"]
