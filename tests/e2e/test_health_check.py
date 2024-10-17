from fastapi.testclient import TestClient


def test_read_root(test_client: TestClient):
    response = test_client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"Health": "Check"}
