"""Services module

提供业务逻辑服务函数
"""

# 也可以导入整个模块
from src.services import user_service

# 导入用户服务的所有函数
from src.services.user_service import (
    create_user,
    delete_user,
    get_all_users,
    get_user_by_id,
    update_user,
)

# 定义公开接口
__all__ = [
    # 用户服务函数
    "get_all_users",
    "get_user_by_id",
    "create_user",
    "update_user",
    "delete_user",
    # 模块
    "user_service",
]
