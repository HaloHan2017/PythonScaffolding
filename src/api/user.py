"""User API endpoints"""

from flask import Blueprint, jsonify

from src.services import UserService

UserController = Blueprint("user", __name__, url_prefix="/api/users")


@UserController.route("", methods=["GET"])
def get_users():
    """Get all users

    Returns:
        JSON response with list of users
    """
    users = UserService.get_all_users()
    return jsonify({"users": [user.model_dump() for user in users]}), 200


@UserController.route("/<int:user_id>", methods=["GET"])
def get_user(user_id: int):
    """Get user by ID

    Args:
        user_id: User ID

    Returns:
        JSON response with user data or error message
    """
    user = UserService.get_user_by_id(user_id)
    if user:
        return jsonify(user.model_dump()), 200
    return jsonify({"error": "User not found"}), 404


@UserController.route("/username/<string:username>", methods=["GET"])
def get_user_by_username(username: str):
    """Get user by username

    Args:
        username: Username

    Returns:
        JSON response with user data or error message
    """
    user = UserService.get_user_by_username(username)
    if user:
        return jsonify(user.model_dump()), 200
    return jsonify({"error": "User not found"}), 404
