from johnathan_url_shortener.adapters.repositories.url import IShortenedURLRepository
from johnathan_url_shortener.services.unit_of_work import IUnitOfWork


class NotFoundShortenedUrlException(Exception):
    pass


def get_shortened_url(uow: IUnitOfWork, token_url: str) -> str:
    with uow:
        url = uow.urls.get(token_url)
        if not url:
            raise NotFoundShortenedUrlException(f"No url found for token '{token_url}'")

        return url
