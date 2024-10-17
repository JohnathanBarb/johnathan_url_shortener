import pytest

from johnathan_url_shortener.services.url.get import (
    get_shortened_url,
    NotFoundShortenedUrlException,
)
from tests.utils.repositories.url import TShortenedURLRepositoryImpl


def test_get_url():

    token_url = "token_url"
    url = "https://my-test-url.com"

    test_url_repository = TShortenedURLRepositoryImpl()
    test_url_repository.INTERNAL_STORAGE[token_url] = url

    returned_url = get_shortened_url(test_url_repository, token_url)

    assert returned_url == url


def test_get_url_when_invalid_token():
    token_url = "invalid_token"

    test_url_repository = TShortenedURLRepositoryImpl()

    with pytest.raises(NotFoundShortenedUrlException):
        get_shortened_url(test_url_repository, token_url)
