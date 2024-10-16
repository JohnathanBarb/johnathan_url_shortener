from fastapi.testclient import TestClient


def test_get_tokenized_url(test_client: TestClient):
    url_to_shorten = "https://blah.com"
    
    response = test_client.post(
        f"/api/v1/url",
        json={"url": url_to_shorten},
    )
    
    assert response.status_code == 200
    assert response.json() == {"url_to_short": url_to_shorten}
