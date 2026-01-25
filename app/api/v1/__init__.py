"""API Version 1"""
from flask import Blueprint
from flask_restx import Api

from app.core.config import settings

# Create blueprint
api_v1 = Blueprint("api_v1", __name__)

# Create API with documentation
api = Api(
    api_v1,
    version="1.0",
    title=settings.PROJECT_NAME,
    description="A modern Flask WebAPI",
    doc="/docs",
    authorizations={
        "Bearer": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
            "description": "Enter: Bearer <token>"
        }
    },
    security="Bearer"
)

# Import and register namespaces
from app.api.v1.endpoints.auth import auth_ns
from app.api.v1.endpoints.users import users_ns
from app.api.v1.endpoints.health import health_ns

api.add_namespace(auth_ns, path="/auth")
api.add_namespace(users_ns, path="/users")
api.add_namespace(health_ns, path="/health")