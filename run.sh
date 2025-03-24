#!/bin/sh

poetry run alembic upgrade head

poetry run uvicorn johnathan_url_shortener.main:app --host 0.0.0.0 --port 8000
