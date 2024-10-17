from johnathan_url_shortener.services.url.get import get_shortened_url
from tests.utils.repositories.url import TShortenedURLRepositoryImpl


def test_get_url():
    
    token_url = "token_url"
    url = "https://my-test-url.com"
    
    test_url_repository = TShortenedURLRepositoryImpl()
    test_url_repository.INTERNAL_STORAGE[token_url] = url
    
    returned_url = get_shortened_url(test_url_repository, token_url)

    assert returned_url == url


# TODO: write test when treat better errors
def test_get_url_when_invalid_token():
    ...
