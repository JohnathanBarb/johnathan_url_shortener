from johnathan_url_shortener.services.unit_of_work import IUnitOfWork


def register_url(uow: IUnitOfWork, url_to_shorten: str) -> str:
    with uow:
        token = uow.urls.register(url_to_shorten)
        return token
