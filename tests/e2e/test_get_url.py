from fastapi.testclient import TestClient


# TODO: fix those tests properly


def test_get_url(test_client: TestClient):

    token_url = "affdasfsa"
    response = test_client.get(f"/api/v1/url/{token_url}")

    assert response.status_code == 200


def test_get_url_when_invalid_token(test_client: TestClient):

    token_url = "doesnotexist"
    response = test_client.get(f"/api/v1/url/{token_url}")

    assert response.status_code == 200
    assert response.json() == {"url": "NOT-FOUND"}
