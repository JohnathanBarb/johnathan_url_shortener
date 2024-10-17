from johnathan_url_shortener.adapters.repositories.url import IShortenedURLRepository


def get_shortened_url(repository: IShortenedURLRepository, token_url: str) -> str:

    url = repository.get(token_url)
    return url
