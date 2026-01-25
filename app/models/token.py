"""Token model for JWT token blacklisting"""
from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base
from app.core.extensions import db


class Token(Base, db.Model):
    """Token model for storing blacklisted tokens"""

    __tablename__ = "tokens"

    # Token information
    jti = Column(String(36), unique=True, index=True, nullable=False)
    token = Column(String(500), nullable=False)
    token_type = Column(String(10), nullable=False)  # access or refresh

    # Expiration
    expires_at = Column(DateTime, nullable=False)

    # Status
    revoked = Column(Boolean, default=False)

    # Relationships
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    user = relationship("User", back_populates="tokens")

    def __repr__(self):
        return f"<Token {self.jti}>"

    @property
    def is_expired(self):
        """Check if token is expired"""
        from datetime import datetime
        return self.expires_at < datetime.utcnow()