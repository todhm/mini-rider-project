import pytest
from fastapi.testclient import TestClient

from app import create_app
from db.base_class import Base
from db.session import get_session, get_test_session, test_engine
from settings import test_settings


@pytest.fixture(scope="function")
def test_app() -> TestClient:
    app = create_app(test_settings)
    app.dependency_overrides[get_session] = get_test_session
    Base.metadata.create_all(test_engine)
    with TestClient(app) as test_client:
        yield test_client
    Base.metadata.drop_all(test_engine)
