"""WSGI entry point for production"""

from . import create_app

# Create app instance for WSGI servers (gunicorn, uwsgi, etc.)
app = create_app()

# For local development only
if __name__ == "__main__":
    # This should ONLY be used for development/testing
    # Use gunicorn or other WSGI server for production
    import os

    app.run(
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", "5000")),
        debug=os.getenv("DEBUG", "False").lower() == "true",
    )
