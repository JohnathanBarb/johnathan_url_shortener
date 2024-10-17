from fastapi.testclient import TestClient


# TODO: fix those tests properly


def test_get_url(test_client: TestClient):

    # register an url to can get it latter
    # TODO: maybe move it to an utils folders

    register_response = test_client.post(
        f"api/v1/url",
        json={"url": "https://www.google.com"},
    )

    token = register_response.json()["token"]

    response = test_client.get(f"/api/v1/url/{token}")

    assert response.status_code == 200
    assert response.json() == {"url": "https://www.google.com"}


def test_get_url_when_invalid_token(test_client: TestClient):

    token_url = "doesnotexist"
    response = test_client.get(f"/api/v1/url/{token_url}")

    assert response.status_code == 404
    assert response.json() == {"detail": "No url found for token 'doesnotexist'"}
