import os

from pydantic import BaseSettings


class TestSettings(BaseSettings):
    DB_URL: str
    app_name: str = "Scooter Test API"
    DEBUG: bool = True


class Settings(BaseSettings):
    app_name: str = "Scooter API App"
    DB_URL: str = os.environ.get("DB_URL")
    DEBUG: bool = False


test_settings = TestSettings(DB_URL=os.environ.get("TEST_DB_URL"))
settings = Settings(DB_URL=os.environ.get("DB_URL"))
