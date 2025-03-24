# URL Shortener



## Setup

### Manual

You need to have Python installed. This project was developed to use python 3.13

1. Clone this repository
2. This project uses Poetry to manage dependencies, see [how use it](https://python-poetry.org/docs/)
and preferably use your best virtualenv tool(I like to use [venv from builtin](https://docs.python.org/3/library/venv.html));
3. Install dependencies: `poetry install`
4. Create a `.env` file on root project, containing:
```
DB_URL=postgresql://JUSDBUSER:JUSDBPASSWORD@jus-db:5432/jus
```

5. For build image, run:
```shell
make build
```

6. For up containers(app and database), run:
```shell
make up
```

7. To run all tests, run:
```shell
make test
```

8. Run for production: IN PROGRESS


### Useful tolls

- To run tests
```shell
make test
```

- To format project files with [Black](https://black.readthedocs.io/en/stable/)
```shell
make format
```

- To generate migrations
```shell
alembic revision --autogenerate -m "YOUR MESSAGE DESCRIBING HERE" 
```
