"""User service layer - Business logic for user operations"""

from src.models.user import User

# Mock user database
MOCK_USERS = [
    User(
        id=1,
        username="johndoe",
        email="john.doe@example.com",
        full_name="John Doe",
        is_active=True,
    ),
    User(
        id=2,
        username="janedoe",
        email="jane.doe@example.com",
        full_name="Jane Doe",
        is_active=True,
    ),
    User(
        id=3,
        username="bobsmith",
        email="bob.smith@example.com",
        full_name="Bob Smith",
        is_active=False,
    ),
]


class UserService:
    """User service for handling user operations"""

    @staticmethod
    def get_all_users() -> list[User]:
        """Get all users"""
        return MOCK_USERS

    @staticmethod
    def get_user_by_id(user_id: int) -> User | None:
        """Get user by ID"""
        for user in MOCK_USERS:
            if user.id == user_id:
                return user
        return None

    @staticmethod
    def get_user_by_username(username: str) -> User | None:
        """Get user by username"""
        for user in MOCK_USERS:
            if user.username == username:
                return user
        return None
