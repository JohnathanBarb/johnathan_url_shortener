from fastapi import FastAPI

from johnathan_url_shortener.routers import v1_router

app = FastAPI(
    title="Johnathan URL Shortener",
    summary="Simple URL Shortener",
)
app.include_router(v1_router)


@app.get(
    "/health",
    description="Health check",
)
def health_check():
    # TODO: implement a better health check
    return {"Health": "Check"}
