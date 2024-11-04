from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from johnathan_url_shortener.adapters.repositories.url import (
    SQLAlchemyShortenedURLRepositoryImpl,
)
from johnathan_url_shortener.dependencies import get_dbsession
from johnathan_url_shortener.services.unit_of_work import (
    IUnitOfWork,
    SqlAlchemyUnitOfWork,
)
from johnathan_url_shortener.services.url.get import (
    get_shortened_url,
    NotFoundShortenedUrlException,
)
from johnathan_url_shortener.services.url.register import register_url

shorten_url_router = APIRouter(prefix="/url")


class URLToShorten(BaseModel):
    url: str


@shorten_url_router.post(
    "/",
    description="Register a shortened URL.",
)
def register_shortened_url(
    url_to_short: URLToShorten, session: Annotated[Session, Depends(get_dbsession)]
):
    token = register_url(
        SqlAlchemyUnitOfWork(session_factory=session),
        url_to_short.url,
    )
    return {"token": token}


@shorten_url_router.get(
    "/{token_url}",
    description="Get a shortened URL.",
)
def get_url(
    token_url: str,
    session: Annotated[Session, Depends(get_dbsession)],
):
    try:

        url = get_shortened_url(
            SqlAlchemyUnitOfWork(session_factory=session),
            token_url,
        )
        return {"url": url}

    except NotFoundShortenedUrlException as e:
        raise HTTPException(status_code=404, detail=str(e))
