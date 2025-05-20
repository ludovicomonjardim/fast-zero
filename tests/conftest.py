from sqlalchemy import create_engine
from src.fast_zero.models import table_registry
from sqlalchemy.orm import Session

from fastapi.testclient import TestClient
from src.fast_zero.database import get_session
from src.fast_zero.app import app
import pytest

@pytest.fixture()
def fix_client(session):

    def get_sesion_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_sesion_override
        yield client

    app.dependency_overrides.clear()

@pytest.fixture()
def fix_session():
    engine = create_engine('sqlite:///:memory:')
    table_registry.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
    table_registry.metadata.drop_all(engine)
