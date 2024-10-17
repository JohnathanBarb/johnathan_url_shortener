from johnathan_url_shortener.adapters.repositories.url import IShortenedURLRepository


class NotFoundShortenedUrlException(Exception):
    pass


def get_shortened_url(repository: IShortenedURLRepository, token_url: str) -> str:
    url = repository.get(token_url)

    if not url:
        raise NotFoundShortenedUrlException(f"No url found for token '{token_url}'")

    return url
