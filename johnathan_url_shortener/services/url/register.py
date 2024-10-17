from johnathan_url_shortener.adapters.repositories.url import IShortenedURLRepository


def register_url(repository: IShortenedURLRepository, url_to_shorten: str) -> str:
    token = repository.register(url_to_shorten)
    return token
