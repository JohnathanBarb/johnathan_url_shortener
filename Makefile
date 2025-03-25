run:
	uv run fastapi dev johnathan_url_shortener/main.py

build:
	docker build -t jus .

up:
	docker compose up -d

down:
	docker compose down

test:
	uv run pytest -s

utest:
	uv run pytest -s tests/unit

itest:
	uv run pytest -s tests/integration

etest:
	uv run pytest -s tests/e2e

format:
	uv run black .

migrate:
	uv run alembic upgrade head
