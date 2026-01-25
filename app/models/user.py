"""User model"""
from datetime import datetime
from sqlalchemy import Boolean, Column, String, DateTime, Enum as SQLEnum
from sqlalchemy.orm import relationship
import enum

from app.models.base import Base
from app.core.extensions import db


class UserRole(enum.Enum):
    """User roles enumeration"""
    USER = "user"
    ADMIN = "admin"
    MODERATOR = "moderator"


class User(Base, db.Model):
    """User model representing application users"""

    __tablename__ = "users"

    # Basic information
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)

    # Authentication
    hashed_password = Column(String(255), nullable=False)

    # Personal information
    full_name = Column(String(100))
    phone_number = Column(String(20))

    # Status
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)

    # Role
    role = Column(SQLEnum(UserRole), default=UserRole.USER)

    # Timestamps
    last_login = Column(DateTime, nullable=True)
    email_verified_at = Column(DateTime, nullable=True)

    # Relationships
    tokens = relationship("Token", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User {self.username}>"

    @property
    def is_admin(self):
        """Check if user is admin"""
        return self.role == UserRole.ADMIN or self.is_superuser

    def to_dict(self, include_sensitive: bool = False):
        """Convert user to dictionary"""
        data = super().to_dict()

        # Remove sensitive data unless requested
        if not include_sensitive:
            data.pop('hashed_password', None)

        # Convert enum to string
        if 'role' in data and data['role']:
            data['role'] = data['role'].value

        return data