import uvicorn
from fastapi import FastAPI

from src.routes import router

app = FastAPI(
    title="Medical Research API",
    version="1.0.0"
)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
