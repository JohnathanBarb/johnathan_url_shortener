from starlette.testclient import TestClient
from pytest import fixture

from johnathan_url_shortener.main import app


@fixture
def test_client() -> TestClient:
    return TestClient(app)
