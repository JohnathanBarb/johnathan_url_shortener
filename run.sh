#!/bin/sh

uv run alembic upgrade head

uv run uvicorn johnathan_url_shortener.main:app --host 0.0.0.0 --port 8000
