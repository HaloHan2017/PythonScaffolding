"""API Version 1 - Hello endpoint"""

from flask import jsonify

from . import api_v1


@api_v1.route("/hello", methods=["GET"])
def hello():
    """Simple hello endpoint"""
    return jsonify({"message": "Hello from API v1!", "version": "1.0"})


@api_v1.route("/ping", methods=["GET"])
def ping():
    """Ping endpoint"""
    return jsonify({"ping": "pong"})
