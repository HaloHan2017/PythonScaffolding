"""User API endpoints"""

from fastapi import APIRouter, HTTPException

from src.models.user import User
from src.services import UserService

UserController = APIRouter(prefix="/api/users", tags=["users"])


@UserController.get("", response_model=dict)
async def get_users():
    """Get all users

    Returns:
        JSON response with list of users
    """
    users = UserService.get_all_users()
    return {"users": [user.model_dump() for user in users]}


@UserController.get("/{user_id}", response_model=User)
async def get_user(user_id: int):
    """Get user by ID

    Args:
        user_id: User ID

    Returns:
        JSON response with user data or error message
    """
    user = UserService.get_user_by_id(user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")


@UserController.get("/username/{username}", response_model=User)
async def get_user_by_username(username: str):
    """Get user by username

    Args:
        username: Username

    Returns:
        JSON response with user data or error message
    """
    user = UserService.get_user_by_username(username)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")
