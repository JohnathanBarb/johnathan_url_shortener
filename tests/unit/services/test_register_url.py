from johnathan_url_shortener.services.url.register import register_url
from tests.utils.unit_of_work import TUnitOfWork


def test_register_url():

    url = "https://my-test-url.com"

    uow = TUnitOfWork()

    url_repository = uow.urls
    token = register_url(uow, url)

    assert url_repository.INTERNAL_STORAGE[token] == url
