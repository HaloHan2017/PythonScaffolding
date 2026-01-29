"""WSGI entry point for cloud"""

import os
import sys

from src import create_app
from src.core.logging import get_logger

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Get logger for this module
logger = get_logger(__name__)

# Create app instance for WSGI servers (gunicorn, uwsgi, etc.)
# database will auto init & connect in create_app()
app = create_app()

# For local development only
if __name__ == "__main__":
    # This should ONLY be used for development/testing
    # Use gunicorn or other WSGI server for cloud

    logger.info("=" * 60)
    logger.info("Starting Flask Application")
    logger.info("=" * 60)
    logger.info(f"Environment: {os.getenv('FLASK_ENV', 'local')}")
    logger.info(f"Database: {os.getenv('DATABASE_URL', 'Not configured')}")
    logger.info(f"Host: {os.getenv('HOST', '0.0.0.0')}")
    logger.info(f"Port: {os.getenv('PORT', '5000')}")
    logger.info("=" * 60)

    app.run(
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", "5000")),
        debug=os.getenv("DEBUG", "False").lower() == "true",
    )
