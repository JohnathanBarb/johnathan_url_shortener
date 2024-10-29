from abc import ABC, abstractmethod

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from johnathan_url_shortener.config import get_settings
from johnathan_url_shortener.adapters.repositories.url import IShortenedURLRepository, InMemoryShortenedURLRepositoryImpl


class IUnitOfWork(ABC):
    urls: IShortenedURLRepository
    
    def __enter__(self) -> "IUnitOfWork":
        return self

    def __exit__(self, *args):
        self.rollback()
    
    @abstractmethod
    def commit(self):
        raise NotImplementedError()
    
    @abstractmethod
    def rollback(self):
        raise NotImplementedError()


engine = create_engine(get_settings().db_url, echo=True)
DEFAULT_SESSION_FACTORY = sessionmaker(bind=engine)

class SqlAlchemyUnitOfWork(IUnitOfWork):
    def __init__(self, session_factory=DEFAULT_SESSION_FACTORY):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        self.urls = InMemoryShortenedURLRepositoryImpl()
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def commit(self):
        self.session.commit()
    
    def rollback(self):
        self.session.rollback()
