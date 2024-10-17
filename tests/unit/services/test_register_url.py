from johnathan_url_shortener.services.url.register import register_url
from tests.utils.repositories.url import TShortenedURLRepositoryImpl


def test_register_url():
    
    url = "https://my-test-url.com"
    
    test_url_repository = TShortenedURLRepositoryImpl()
    token = register_url(test_url_repository, url)
    
    assert test_url_repository.INTERNAL_STORAGE[token] == url
