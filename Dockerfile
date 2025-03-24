FROM python:3.13-alpine

WORKDIR /app

RUN apk add build-base libpq libpq-dev

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY alembic.ini ./alembic.ini
COPY johnathan_url_shortener ./johnathan_url_shortener
COPY run.sh ./run.sh

RUN chmod +x ./run.sh

CMD ["./run.sh"]
