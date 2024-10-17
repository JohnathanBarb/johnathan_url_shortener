from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from johnathan_url_shortener.adapters.repositories.url import (
    InMemoryShortenedURLRepositoryImpl,
)
from johnathan_url_shortener.services.url.get import (
    get_shortened_url,
    NotFoundShortenedUrlException,
)
from johnathan_url_shortener.services.url.register import register_url

shorten_url_router = APIRouter(
    prefix="/url",
    tags=["url"],
)


class URLToShorten(BaseModel):
    url: str


@shorten_url_router.post("/")
def shorten_url(url_to_short: URLToShorten):
    token = register_url(
        InMemoryShortenedURLRepositoryImpl(),
        url_to_short.url,
    )
    return {"token": token}


@shorten_url_router.get("/{token_url}")
def get_url(token_url: str):
    try:

        url = get_shortened_url(
            InMemoryShortenedURLRepositoryImpl(),
            token_url,
        )
        return {"url": url}

    except NotFoundShortenedUrlException as e:
        raise HTTPException(status_code=404, detail=str(e))
