from fastapi import FastAPI
from typing import Dict

app = FastAPI()


@app.get("/")
async def root() -> Dict[str, str]:
    return {"message": "Hello World"}


@app.get("/health")
async def health() -> Dict[str, str]:
    return {"status": "ok"}