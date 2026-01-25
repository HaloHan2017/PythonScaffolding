"""Unit tests for users"""
import pytest
from app.models.user import User


def test_user_creation():
    """Test user creation"""
    user = User(
        username="testuser",
        email="test@example.com",
        hashed_password="hashed"
    )

    assert user.username == "testuser"
    assert user.email == "test@example.com"
    assert user.is_active is True
    assert user.role.value == "user"


def test_user_to_dict():
    """Test user to_dict method"""
    user = User(
        username="testuser",
        email="test@example.com",
        hashed_password="hashed"
    )

    user_dict = user.to_dict()

    assert "username" in user_dict
    assert "email" in user_dict
    assert "hashed_password" not in user_dict  # Sensitive data excluded


def test_user_is_admin():
    """Test admin check"""
    user = User(username="user", email="user@example.com", hashed_password="hashed")
    admin = User(username="admin", email="admin@example.com", hashed_password="hashed")
    admin.role = "admin"

    assert not user.is_admin
    assert admin.is_admin