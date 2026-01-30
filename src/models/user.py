"""User data models"""

from pydantic import BaseModel, Field


class User(BaseModel):
    """User model"""

    id: int = Field(..., description="User ID")
    username: str = Field(..., min_length=3, max_length=50, description="Username")
    email: str = Field(..., description="Email address")
    full_name: str | None = Field(None, description="Full name")
    is_active: bool = Field(default=True, description="Is user active")

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "username": "johndoe",
                "email": "john.doe@example.com",
                "full_name": "John Doe",
                "is_active": True,
            }
        }
