from fastapi import FastAPI
from johnathan_url_shortener.routers import v1_router


app = FastAPI()
app.include_router(v1_router)

@app.get("/")
def root():
    return {"Hello": "World"}
