"""Error handlers for Flask application"""

from flask import Flask
from werkzeug.exceptions import HTTPException

from src.core.exceptions import APIException
from src.core.response import error_response


def register_error_handlers(app: Flask):
    """Register error handlers"""

    @app.errorhandler(APIException)
    def handle_api_exception(error: APIException):
        """Handle custom API exceptions"""
        app.logger.warning(f"API Exception: {error.message}")
        return error_response(
            message=error.message,
            status_code=error.status_code,
            errors=error.payload.get("errors") if error.payload else None,
        )

    @app.errorhandler(HTTPException)
    def handle_http_exception(error: HTTPException):
        """Handle Werkzeug HTTP exceptions"""
        return error_response(
            message=error.description or "An error occurred",
            status_code=error.code or 500,
        )

    @app.errorhandler(404)
    def not_found(error):
        return error_response(
            message="The requested resource was not found",
            status_code=404,
        )

    @app.errorhandler(500)
    def internal_error(error):
        app.logger.error(f"Server Error: {error}")
        return error_response(
            message="An unexpected error occurred",
            status_code=500,
        )

    @app.errorhandler(400)
    def bad_request(error):
        return error_response(message="Invalid request", status_code=400)

    @app.errorhandler(403)
    def forbidden(error):
        return error_response(message="Access denied", status_code=403)

    @app.errorhandler(405)
    def method_not_allowed(error):
        return error_response(
            message="The method is not allowed for the requested URL",
            status_code=405,
        )

    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        """Handle unexpected errors"""
        app.logger.exception(f"Unexpected error: {error}")
        return error_response(
            message="An unexpected error occurred",
            status_code=500,
        )
