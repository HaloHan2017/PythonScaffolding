"""ASGI entry point for production"""

from . import create_app

# Create app instance for ASGI servers (gunicorn + uvicorn, uvicorn, etc.)
app = create_app()

# For local development only
if __name__ == "__main__":
    # This should ONLY be used for development/testing
    # Use gunicorn + uvicorn or uvicorn for production
    import os

    import uvicorn

    uvicorn.run(
        "src.app:app",
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", "8000")),
        reload=os.getenv("DEBUG", "False").lower() == "true",
    )
