"""Database management using Peewee ORM"""

from contextvars import ContextVar
from functools import wraps
from typing import Any, Optional

from flask import Flask, g
from peewee import (  # type: ignore[import-untyped]
    Database,
    Model,
    MySQLDatabase,
    SqliteDatabase,
)

from src.core.config import settings
from src.core.logging import get_logger

logger = get_logger(__name__)

# Context variable for database connection
_db_state = ContextVar("db_state", default=None)

# Global database instance
db: Optional[Database] = None


def get_database_instance() -> Database:
    """
    Create and return database instance based on DATABASE_URL

    Supports:
        - PostgreSQL: postgresql://user:pass@host:port/dbname
        - MySQL: mysql://user:pass@host:port/dbname
        - SQLite: sqlite:///path/to/db.db

    Returns:
        Database instance
    """
    if not settings.DATABASE_URL:
        logger.warning("DATABASE_URL not set, using in-memory SQLite")
        return SqliteDatabase(":memory:")

    url = settings.DATABASE_URL.lower()

    if url:
        # Parse MySQL URL
        from urllib.parse import urlparse

        parsed = urlparse(settings.DATABASE_URL)
        return MySQLDatabase(
            parsed.path[1:],
            user=parsed.username,
            password=parsed.password,
            host=parsed.hostname,
            port=parsed.port or 3306,
            charset="utf8mb4",
        )
    else:
        raise ValueError(f"Unsupported database URL: {settings.DATABASE_URL}")


def init_database(app: Flask) -> Database:
    """
    Initialize database and register Flask hooks

    Args:
        app: Flask application instance

    Returns:
        Database instance
    """
    global db

    db = get_database_instance()
    logger.info(f"Database initialized: {db.__class__.__name__}")

    # Register request hooks
    @app.before_request
    def _db_connect():
        """Connect to database before each request"""
        if db.is_closed():
            db.connect()
            logger.debug("Database connected")
        # Store connection state
        g._db_connected = True

    @app.teardown_request
    def _db_close(exc):
        """Close database connection after each request"""
        if not db.is_closed():
            db.close()
            logger.debug("Database closed")
        g._db_connected = False

    return db


def get_db() -> Database:
    if db is None:
        raise RuntimeError("Database not initialized. Call init_database(app) first.")
    return db


class BaseModel(Model):
    _meta: Any

    class Meta:
        database = None  # Will be set dynamically

    @classmethod
    def set_database(cls, database: Database):
        """Set database for this model and all subclasses"""
        cls._meta.database = database
        # Recursively set database for all subclasses
        for subclass in cls.__subclasses__():
            subclass._meta.database = database
            # Also set for nested subclasses
            subclass.set_database(database)


def atomic():
    """
    Decorator for atomic database operations (transaction)

    Example:
        @atomic()
        def create_user_and_profile(user_data, profile_data):
            user = User.create(**user_data)
            profile = Profile.create(user=user, **profile_data)
            return user
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if db is None:
                raise RuntimeError("Database not initialized")

            with db.atomic():
                return func(*args, **kwargs)

        return wrapper

    return decorator


def transaction():
    """
    Context manager for database transactions

    Example:
        with transaction():
            User.create(username='john')
            Post.create(title='Hello')
    """
    if db is None:
        raise RuntimeError("Database not initialized")

    return db.atomic()


def check_database_connection() -> bool:
    try:
        if db is None:
            return False

        # Try to execute a simple query
        db.execute_sql("SELECT 1")
        return True

    except Exception as e:
        logger.error(f"Database connection check failed: {e}")
        return False


def close_database():
    if db and not db.is_closed():
        db.close()
        logger.info("Database connection closed")


# Health check function
def database_health() -> dict:
    if db is None:
        return {"status": "not_initialized", "healthy": False}

    try:
        is_connected = check_database_connection()
        return {
            "status": "healthy" if is_connected else "unhealthy",
            "healthy": is_connected,
            "database_type": db.__class__.__name__,
            "is_closed": db.is_closed(),
        }
    except Exception as e:
        return {"status": "error", "healthy": False, "error": str(e)}
