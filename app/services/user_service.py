"""User service for business logic"""
from typing import Optional, List
from datetime import datetime

from app.core.extensions import db
from app.models.user import User, UserRole
from app.core.security import Security


class UserService:
    """Service for user-related operations"""

    @staticmethod
    def get_all_users() -> List[User]:
        """Get all users"""
        return User.query.filter_by(is_active=True).all()

    @staticmethod
    def get_user_by_id(user_id: int) -> Optional[User]:
        """Get user by ID"""
        return User.query.get(user_id)

    @staticmethod
    def get_user_by_email(email: str) -> Optional[User]:
        """Get user by email"""
        return User.query.filter_by(email=email.lower()).first()

    @staticmethod
    def get_user_by_username(username: str) -> Optional[User]:
        """Get user by username"""
        return User.query.filter_by(username=username.lower()).first()

    @staticmethod
    def create_user(user_data: dict) -> User:
        """Create a new user"""
        user = User(
            username=user_data.get("username").lower(),
            email=user_data.get("email").lower(),
            hashed_password=Security.hash_password(user_data.get("password")),
            full_name=user_data.get("full_name"),
            phone_number=user_data.get("phone_number"),
            is_active=True,
            role=UserRole.USER
        )

        db.session.add(user)
        db.session.commit()

        return user

    @staticmethod
    def update_user(user_id: int, update_data: dict) -> Optional[User]:
        """Update user information"""
        user = User.query.get(user_id)
        if not user:
            return None

        # Update allowed fields
        allowed_fields = ["full_name", "phone_number", "is_active"]
        for field in allowed_fields:
            if field in update_data:
                setattr(user, field, update_data[field])

        user.updated_at = datetime.utcnow()
        db.session.commit()

        return user

    @staticmethod
    def delete_user(user_id: int) -> bool:
        """Delete a user (soft delete)"""
        user = User.query.get(user_id)
        if not user:
            return False

        # Soft delete
        user.is_active = False
        user.updated_at = datetime.utcnow()
        db.session.commit()

        return True

    @staticmethod
    def create_admin() -> User:
        """Create admin user (for initial setup)"""
        admin_data = {
            "username": "admin",
            "email": "admin@example.com",
            "password": "Admin123!",
            "full_name": "Administrator",
            "role": UserRole.ADMIN,
            "is_superuser": True,
            "is_verified": True
        }

        # Check if admin already exists
        existing_admin = User.query.filter_by(email=admin_data["email"]).first()
        if existing_admin:
            return existing_admin

        user = User(
            username=admin_data["username"],
            email=admin_data["email"],
            hashed_password=Security.hash_password(admin_data["password"]),
            full_name=admin_data["full_name"],
            role=admin_data["role"],
            is_superuser=admin_data["is_superuser"],
            is_verified=admin_data["is_verified"],
            is_active=True
        )

        db.session.add(user)
        db.session.commit()

        return user