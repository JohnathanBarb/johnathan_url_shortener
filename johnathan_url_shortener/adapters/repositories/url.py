from abc import ABC, abstractmethod
from typing import Dict, Optional

from sqlalchemy import select, insert

from johnathan_url_shortener.adapters.database.url import URL
from johnathan_url_shortener.utils import generate_token


class IShortenedURLRepository(ABC):
    @abstractmethod
    def register(self, shortened_url: str) -> str:
        raise NotImplementedError()

    @abstractmethod
    def get(self, url_token: str) -> Optional[str]:
        raise NotImplementedError()


my_database: Dict[str, str] = {}


class SQLAlchemyShortenedURLRepositoryImpl(IShortenedURLRepository):
    def __init__(self, dbsession):
        self.dbsession = dbsession

    def register(self, shortened_url: str) -> str:
        # generate a token to be identifier to shortened url

        token_shortened_url = generate_token()

        url_stmt = insert(URL).values(
            {
                "token": token_shortened_url,
                "url": shortened_url,
            }
        )
        self.dbsession.execute(url_stmt)

        return token_shortened_url

    def get(self, url_token: str) -> Optional[str]:
        url_stmt = select(URL.c.url).filter(URL.c.token == url_token)
        url = self.dbsession.execute(url_stmt).first()

        # TODO: think better on handling not found exception
        return None if url is None else url.url
