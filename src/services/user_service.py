"""User service layer using Peewee ORM"""

from typing import List, Optional, Tuple

from src.core.database import atomic
from src.core.exceptions import NotFoundError
from src.core.logging import get_logger
from src.models.user_model import UserModel

logger = get_logger(__name__)


# 直接使用函数，不需要类包装
def get_all_users() -> Tuple[List[UserModel], int]:
    try:
        query = UserModel.select().order_by(UserModel.id.desc())
        total = query.count()
        users = list(query)
        return users, total
    except Exception as e:
        logger.error(f"Error fetching users: {e}")
        return [], 0


def get_user_by_id(user_id: int) -> Optional[UserModel]:
    try:
        return UserModel.get_by_id(user_id)
    except Exception as e:
        logger.error(f"Error fetching user {user_id}: {e}")
        return None


@atomic()
def create_user(name: str, age: Optional[int] = None) -> UserModel:
    user = UserModel.create(name=name, age=age)
    logger.info(f"User created: {user.name} (ID: {user.id})")
    return user


@atomic()
def update_user(user_id: int, **kwargs) -> UserModel:
    user = get_user_by_id(user_id)
    if not user:
        raise NotFoundError(f"User {user_id} not found")

    # Update fields
    for key, value in kwargs.items():
        if hasattr(user, key) and key not in ["id"]:
            setattr(user, key, value)

    user.save()
    logger.info(f"User updated: {user.name} (ID: {user.id})")
    return user


@atomic()
def delete_user(user_id: int) -> None:
    user = get_user_by_id(user_id)
    if not user:
        raise NotFoundError(f"User {user_id} not found")

    name = user.name
    user.delete_instance()
    logger.info(f"User deleted: {name} (ID: {user_id})")
