FROM python:3.13-alpine
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

RUN apk add build-base libpq libpq-dev

COPY pyproject.toml uv.lock ./

RUN uv sync

COPY alembic.ini ./alembic.ini
COPY johnathan_url_shortener ./johnathan_url_shortener
COPY run.sh ./run.sh

RUN chmod +x ./run.sh

CMD ["./run.sh"]
