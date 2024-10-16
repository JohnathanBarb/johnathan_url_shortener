from fastapi import APIRouter
from pydantic import BaseModel

shorten_url_router = APIRouter(
    prefix="/url",
    tags=["url"],
)


class URLToShorten(BaseModel):
    url: str


@shorten_url_router.post("/")
def shorten_url(url_to_short: URLToShorten):
    return {"url_to_short": url_to_short.url}


@shorten_url_router.get("/{shortened_url}")
def get_shortened_url(shortened_url: str):
    return {"shortened_url": shortened_url}
