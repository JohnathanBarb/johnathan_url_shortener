from johnathan_url_shortener.services.unit_of_work import IUnitOfWork
from tests.utils.repositories.url import TShortenedURLRepositoryImpl


class TUnitOfWork(IUnitOfWork):
    def __init__(self):
        self.urls = TShortenedURLRepositoryImpl()

    def commit(self):
        ...
    
    def rollback(self):
        ...
