"""Error handlers for Flask application"""

from flask import Flask, jsonify


def register_error_handlers(app: Flask):
    """Register error handlers"""

    @app.errorhandler(404)
    def not_found(error):
        return (
            jsonify(
                {
                    "error": "Not Found",
                    "message": "The requested resource was not found",
                }
            ),
            404,
        )

    @app.errorhandler(500)
    def internal_error(error):
        app.logger.error(f"Server Error: {error}")
        return (
            jsonify(
                {
                    "error": "Internal Server Error",
                    "message": "An unexpected error occurred",
                }
            ),
            500,
        )

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"error": "Bad Request", "message": "Invalid request"}), 400

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({"error": "Forbidden", "message": "Access denied"}), 403

    @app.errorhandler(405)
    def method_not_allowed(error):
        return (
            jsonify(
                {
                    "error": "Method Not Allowed",
                    "message": "The method is not allowed for the requested URL",
                }
            ),
            405,
        )
