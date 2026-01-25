"""Database configuration"""
from contextlib import contextmanager

from app.core.extensions import db


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = db.session
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def init_db():
    """Initialize database"""
    # Create tables
    db.create_all()

    # Import models to ensure they are registered
    from app.models import user, token

    print("Database initialized")


def drop_db():
    """Drop all tables"""
    db.drop_all()
    print("Database dropped")