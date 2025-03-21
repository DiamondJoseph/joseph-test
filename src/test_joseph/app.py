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

    return app
