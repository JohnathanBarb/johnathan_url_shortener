run:
	poetry run fastapi dev johnathan_url_shortener/main.py

up:
	docker compose up -d

down:
	docker compose down

test:
	poetry run pytest -s

utest:
	poetry run pytest -s tests/unit

itest:
	poetry run pytest -s tests/integration

etest:
	poetry run pytest -s tests/e2e

format:
	poetry run black .

migrate:
	poetry run alembic upgrade head
