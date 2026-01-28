"""WSGI entry point for cloud"""

import os
import sys

from src import create_app

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Create app instance for WSGI servers (gunicorn, uwsgi, etc.)
# database will auto init & connect in create_app()
app = create_app()

# For local development only
if __name__ == "__main__":
    # This should ONLY be used for development/testing
    # Use gunicorn or other WSGI server for cloud

    print("=" * 60)
    print("Starting Flask Application")
    print("=" * 60)
    print(f"Environment: {os.getenv('FLASK_ENV', 'local')}")
    print(f"Database: {os.getenv('DATABASE_URL', 'Not configured')}")
    print(f"Host: {os.getenv('HOST', '0.0.0.0')}")
    print(f"Port: {os.getenv('PORT', '5000')}")
    print("=" * 60)
    print()

    app.run(
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", "5000")),
        debug=os.getenv("DEBUG", "False").lower() == "true",
    )
