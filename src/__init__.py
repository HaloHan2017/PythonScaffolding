"""Application Factory Pattern"""

import os

from flask import Flask, jsonify


def create_app() -> Flask:
    """Create Flask application"""
    app = Flask(__name__)

    # Load configuration
    app.config["DEBUG"] = os.getenv("DEBUG", "False").lower() == "true"
    app.config["ENV"] = os.getenv("FLASK_ENV", "development")

    # Register blueprints
    register_blueprints(app)

    # Health check endpoint
    @app.route("/")
    def index():
        return jsonify(
            {"name": "Flask API Scaffold", "version": "1.0.0", "status": "running"}
        )

    @app.route("/health")
    def health():
        return jsonify({"status": "healthy"}), 200

    return app


def register_blueprints(app: Flask):
    """Register API blueprints"""
    from src.api.user import UserController

    app.register_blueprint(UserController)
