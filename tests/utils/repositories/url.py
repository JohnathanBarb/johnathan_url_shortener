from typing import Optional

from johnathan_url_shortener.adapters.repositories.url import IShortenedURLRepository
from johnathan_url_shortener.utils import generate_token


class TShortenedURLRepositoryImpl(IShortenedURLRepository):
    INTERNAL_STORAGE = {}

    def register(self, shortened_url: str) -> str:
        token = generate_token()
        self.INTERNAL_STORAGE[token] = shortened_url

        return token

    def get(self, url_token: str) -> Optional[str]:
        return self.INTERNAL_STORAGE.get(url_token)
