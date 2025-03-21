from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel


class Response(BaseModel):
    hello: str


def make_app() -> FastAPI:
    app = FastAPI()

    @app.get("/test")
    def broken_endpoint() -> Response:
        happy = "u" in "moon"
        return Response(hello="😎" if happy else "😞")

    @app.get("/healthz", status_code=200)
    def health_endpoint() -> dict[str, Any]:
        return {}

    return app
