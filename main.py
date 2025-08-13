from fastapi import FastAPI
from fastapi.responses import PlainTextResponse


app = FastAPI(openapi_url=None, docs_url=None, redoc_url=None)


@app.get("/ping", response_class=PlainTextResponse)
async def ping() -> str:
	return "pong"

