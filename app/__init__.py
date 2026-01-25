"""Application Factory Pattern"""
from flask import Flask, jsonify
from flask_cors import CORS

from app.core.config import settings
from app.core.extensions import db, migrate, jwt, limiter, cache
from app.api.v1 import api_v1


def create_app(config_name: str = "development") -> Flask:
    """Create Flask application"""
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(f"app.core.config.{config_name.capitalize()}Config")

    # Initialize extensions
    initialize_extensions(app)

    # Register blueprints
    register_blueprints(app)

    # Register error handlers
    register_error_handlers(app)

    # Register CLI commands
    register_commands(app)

    # Add health check endpoint
    @app.route("/")
    def index():
        return jsonify({
            "name": settings.PROJECT_NAME,
            "version": settings.VERSION,
            "environment": settings.ENVIRONMENT,
            "docs": f"{app.config.get('BASE_URL', '')}/docs"
        })

    return app


def initialize_extensions(app: Flask):
    """Initialize Flask extensions"""
    # CORS
    CORS(app, origins=settings.BACKEND_CORS_ORIGINS)

    # Database
    db.init_app(app)

    # Migrations
    migrate.init_app(app, db)

    # JWT
    jwt.init_app(app)

    # Rate Limiter
    limiter.init_app(app)

    # Cache
    cache.init_app(app)


def register_blueprints(app: Flask):
    """Register API blueprints"""
    app.register_blueprint(api_v1, url_prefix=settings.API_V1_STR)


def register_error_handlers(app: Flask):
    """Register error handlers"""

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "error": "Not Found",
            "message": "The requested resource was not found"
        }), 404

    @app.errorhandler(500)
    def internal_error(error):
        app.logger.error(f"Server Error: {error}")
        return jsonify({
            "error": "Internal Server Error",
            "message": "An unexpected error occurred"
        }), 500

    @app.errorhandler(429)
    def rate_limit_exceeded(error):
        return jsonify({
            "error": "Too Many Requests",
            "message": "Rate limit exceeded"
        }), 429


def register_commands(app: Flask):
    """Register CLI commands"""

    @app.cli.command("create-admin")
    def create_admin():
        """Create an admin user"""
        from app.services.user_service import UserService
        UserService.create_admin()
        print("Admin user created")

    @app.cli.command("seed-db")
    def seed_db():
        """Seed database with sample data"""
        from scripts.seed import seed_database
        seed_database()
        print("Database seeded")