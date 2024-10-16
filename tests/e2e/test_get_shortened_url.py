from fastapi.testclient import TestClient


def test_get_tokenized_url(test_client: TestClient):

    tokenized_url = "affdasfsa"
    response = test_client.get(f"/api/v1/url/{tokenized_url}")

    assert response.status_code == 200
    assert response.json() == {"shortened_url": tokenized_url}
