"""Pytest configuration"""
import pytest
from flask import Flask

from app import create_app
from app.core.extensions import db as _db


@pytest.fixture(scope="session")
def app():
    """Create application for testing"""
    app = create_app("testing")

    with app.app_context():
        yield app


@pytest.fixture(scope="session")
def db(app: Flask):
    """Create database for testing"""
    _db.create_all()

    yield _db

    _db.drop_all()


@pytest.fixture(scope="function")
def session(db):
    """Create database session"""
    connection = db.engine.connect()
    transaction = connection.begin()

    session = db.create_scoped_session(
        options={"bind": connection, "binds": {}}
    )

    db.session = session

    yield session

    transaction.rollback()
    connection.close()
    session.remove()


@pytest.fixture
def client(app, session):
    """Create test client"""
    with app.test_client() as client:
        yield client


@pytest.fixture
def auth_headers():
    """Create authentication headers"""

    def _auth_headers(token):
        return {"Authorization": f"Bearer {token}"}

    return _auth_headers