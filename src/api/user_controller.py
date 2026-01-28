"""User API endpoints"""

from flask import Blueprint, request

from src.core.exceptions import NotFoundError, ValidationError
from src.core.logging import get_logger
from src.core.response import created_response, success_response
from src.services import user_service  # 导入整个模块

logger = get_logger(__name__)

UserController = Blueprint("user", __name__, url_prefix="/api/users")


@UserController.route("", methods=["GET"])
def get_users():
    """Get all users"""
    logger.info("Fetching all users")

    users, total = user_service.get_all_users()

    return success_response(
        data=[user.to_dict() for user in users],
        message="Users retrieved successfully",
    )


@UserController.route("/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id: int):
    logger.info(f"Fetching user: {user_id}")
    user = user_service.get_user_by_id(user_id)

    if not user:
        raise NotFoundError(f"User with ID {user_id} not found")

    return success_response(data=user.to_dict(), message="User retrieved successfully")


@UserController.route("", methods=["POST"])
def create_user():
    """Create a new user"""
    data = request.get_json()

    if not data:
        raise ValidationError("Request body is required")

    # Validate required fields
    name = data.get("name")
    if not name:
        raise ValidationError("Name is required")

    # Optional fields
    age = data.get("age")

    logger.info(f"Creating user: {name}")
    user = user_service.create_user(name=name, age=age)

    return created_response(
        data=user.to_dict(),
        message="User created successfully",
    )


@UserController.route("/<int:user_id>", methods=["PUT", "PATCH"])
def update_user(user_id: int):
    """Update user by ID"""
    data = request.get_json()

    if not data:
        raise ValidationError("Request body is required")

    logger.info(f"Updating user: {user_id}")
    user = user_service.update_user(user_id, **data)

    return success_response(
        data=user.to_dict(),
        message="User updated successfully",
    )


@UserController.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id: int):
    """Delete user by ID"""
    logger.info(f"Deleting user: {user_id}")
    user_service.delete_user(user_id)

    return success_response(
        data={"id": user_id},
        message="User deleted successfully",
    )
