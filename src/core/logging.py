"""Logging configuration and utilities"""

import logging
import sys

from flask import Flask, has_request_context, request


class RequestFormatter(logging.Formatter):
    """Custom formatter that includes request context"""

    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.method = request.method
            record.ip = request.remote_addr
        else:
            record.url = None
            record.method = None
            record.ip = None

        return super().format(record)


def setup_logging(
    app: Flask,
    log_level: str = "INFO",
    json_format: bool = False,
):
    """
    Setup application logging

    Args:
        app: Flask application instance
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        json_format: Whether to use JSON format for logs (requires python-json-logger)
    """
    # Get log level
    level = getattr(logging, log_level.upper(), logging.INFO)

    # Create formatter
    formatter: logging.Formatter
    if json_format:
        try:
            from pythonjsonlogger import jsonlogger

            formatter = jsonlogger.JsonFormatter(
                "%(asctime)s %(levelname)s %(name)s %(message)s %(url)s %(method)s %(ip)s"
            )
        except ImportError:
            app.logger.warning(
                "python-json-logger not installed, falling back to standard format"
            )
            formatter = RequestFormatter(
                "[%(asctime)s] %(levelname)s in %(module)s: %(message)s [%(method)s %(url)s from %(ip)s]"
            )
    else:
        formatter = RequestFormatter(
            "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
        )

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)

    # Configure app logger
    app.logger.setLevel(level)
    app.logger.addHandler(console_handler)

    # Disable default Flask logger
    app.logger.propagate = False

    # Log startup
    app.logger.info(f"Logging initialized - Level: {log_level}")


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
