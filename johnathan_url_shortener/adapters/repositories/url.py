from abc import ABC, abstractmethod
from typing import Dict

from johnathan_url_shortener.utils import generate_token


class IShortenedURLRepository(ABC):
    @abstractmethod
    def register(self, shortened_url: str) -> str:
        raise NotImplementedError()

    @abstractmethod
    def get(self, url_token: str) -> str:
        raise NotImplementedError()


my_database: Dict[str, str] = {}


class InMemoryShortenedURLRepositoryImpl(IShortenedURLRepository):
    def register(self, shortened_url: str) -> str:
        # generate a token to be identifier to shortened url

        token_shortened_url = generate_token()
        my_database[token_shortened_url] = shortened_url

        return token_shortened_url

    def get(self, url_token: str) -> str:
        return my_database.get(url_token, "NOT-FOUND")
