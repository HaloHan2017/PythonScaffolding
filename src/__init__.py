"""Application Factory Pattern"""

from flask import Flask

from src.core.config import settings
from src.core.database import database_health, init_database
from src.core.logging import setup_logging
from src.core.response import success_response


def create_app() -> Flask:
    """Create Flask application"""
    app = Flask(__name__)

    # Load configuration from settings
    app.config["DEBUG"] = settings.DEBUG
    app.config["ENV"] = "local" if settings.DEBUG else "cloud"

    # Setup logging
    setup_logging(
        app,
        log_level=settings.LOG_LEVEL,
    )

    app.logger.info(f"Starting {settings.APP_NAME}")

    # Initialize database (连接数据库并设置连接池管理)
    db = init_database(app)

    # Import all models first (so they are registered as BaseModel subclasses)
    from src.core.database import BaseModel
    from src.models.user_model import UserModel  # noqa: F401

    # Set database for all models that inherit from BaseModel
    BaseModel.set_database(db)

    app.logger.info(f"Database initialized: {db.__class__.__name__}")

    # Register blueprints
    register_blueprints(app)

    # Register error handlers
    from src.core.error_handlers import register_error_handlers

    register_error_handlers(app)

    # Health check endpoint
    @app.route("/")
    def index():
        return success_response(
            data={
                "name": settings.APP_NAME,
                "status": "running",
            },
            message="API is running",
        )

    @app.route("/health")
    def health():
        return success_response(
            data={"status": "healthy"}, message="Service is healthy"
        )

    @app.route("/health/db")
    def health_db():
        """Database health check"""
        health_status = database_health()
        status_code = 200 if health_status["healthy"] else 503
        return (
            success_response(data=health_status, message="Database health check"),
            status_code,
        )

    return app


def register_blueprints(app: Flask):
    """Register API blueprints"""
    from src.api.user_controller import UserController

    app.register_blueprint(UserController)
