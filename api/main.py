from fastapi import FastAPI

import uvicorn

app = FastAPI()


@app.get("/ping")
async def ping():
    return "hello"

