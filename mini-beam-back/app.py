from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseSettings

from api.scooters import scooterapp


def create_app(settings: BaseSettings) -> FastAPI:
    app = FastAPI(debug=settings.DEBUG)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(scooterapp)
    return app
