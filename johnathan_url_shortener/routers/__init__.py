from fastapi import APIRouter
from johnathan_url_shortener.routers.url.router import shorten_url_router


v1_router = APIRouter(
    prefix="/api/v1",
    tags=["api", "v1"],
    responses={404: {"description": "Not found"}},
)

v1_router.include_router(shorten_url_router)
