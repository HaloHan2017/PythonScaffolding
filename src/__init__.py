"""Application Factory Pattern"""

import os

from fastapi import FastAPI


def create_app() -> FastAPI:
    """Create FastAPI application"""
    app = FastAPI(
        title="FastAPI API Scaffold",
        version="1.0.0",
        description="A modern FastAPI WebAPI scaffold",
        debug=os.getenv("DEBUG", "False").lower() == "true",
    )

    # Register routers
    register_routers(app)

    # Health check endpoints
    @app.get("/", tags=["root"])
    async def index():
        return {"name": "FastAPI API Scaffold", "version": "1.0.0", "status": "running"}

    @app.get("/health", tags=["health"])
    async def health():
        return {"status": "healthy"}

    return app


def register_routers(app: FastAPI):
    """Register API routers"""
    from src.api.user import UserController

    app.include_router(UserController)
