import pytest

from johnathan_url_shortener.services.url.get import (
    get_shortened_url,
    NotFoundShortenedUrlException,
)
from tests.utils.unit_of_work import TUnitOfWork


def test_get_url():

    token_url = "token_url"
    url = "https://my-test-url.com"
    
    uow = TUnitOfWork()

    test_url_repository = uow.urls
    test_url_repository.INTERNAL_STORAGE[token_url] = url

    returned_url = get_shortened_url(TUnitOfWork(), token_url)
    
    assert returned_url == url


def test_get_url_when_invalid_token():
    token_url = "invalid_token"

    with pytest.raises(NotFoundShortenedUrlException):
        get_shortened_url(TUnitOfWork(), token_url)
