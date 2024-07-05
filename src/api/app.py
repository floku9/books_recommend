from fastapi import FastAPI
import uvicorn

from api.routes import authors

app = FastAPI(
    title="Books Library API",
    description="API for Books Library",
    version="0.0.1",
)

app.include_router(authors.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)