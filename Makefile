run:
	poetry run fastapi dev johnathan_url_shortener/main.py

test:
	poetry run pytest -s

format:
	poetry run black .
