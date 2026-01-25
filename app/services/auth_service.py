"""Authentication service"""
from datetime import datetime, timedelta
from typing import Optional
from uuid import uuid4

from app.core.extensions import db
from app.models.user import User
from app.models.token import Token
from app.core.security import Security


class AuthService:
    """Service for authentication operations"""

    @staticmethod
    def authenticate_user(username: str, password: str) -> Optional[User]:
        """Authenticate user with username and password"""
        user = User.query.filter_by(username=username.lower()).first()
        if not user:
            return None

        if not user.is_active:
            return None

        if not Security.verify_password(password, user.hashed_password):
            return None

        return user

    @staticmethod
    def store_tokens(user: User, access_token: str, refresh_token: str):
        """Store tokens in database for blacklisting"""
        # Decode tokens to get expiration
        access_payload = Security.verify_token(access_token)
        refresh_payload = Security.verify_token(refresh_token)

        if access_payload:
            access_token_record = Token(
                jti=access_payload.get("jti", str(uuid4())),
                token=access_token,
                token_type="access",
                expires_at=datetime.fromtimestamp(access_payload["exp"]),
                user_id=user.id
            )
            db.session.add(access_token_record)

        if refresh_payload:
            refresh_token_record = Token(
                jti=refresh_payload.get("jti", str(uuid4())),
                token=refresh_token,
                token_type="refresh",
                expires_at=datetime.fromtimestamp(refresh_payload["exp"]),
                user_id=user.id
            )
            db.session.add(refresh_token_record)

        db.session.commit()

    @staticmethod
    def verify_refresh_token(refresh_token: str) -> Optional[int]:
        """Verify refresh token and return user ID"""
        payload = Security.verify_token(refresh_token)
        if not payload:
            return None

        # Check if token is blacklisted
        jti = payload.get("jti")
        token_record = Token.query.filter_by(jti=jti, revoked=False).first()
        if token_record and token_record.is_expired:
            return None

        return int(payload.get("sub"))

    @staticmethod
    def revoke_token(jti: str):
        """Revoke a token by its JTI"""
        token = Token.query.filter_by(jti=jti).first()
        if token:
            token.revoked = True
            db.session.commit()

    @staticmethod
    def get_user_by_id(user_id: int) -> Optional[User]:
        """Get user by ID"""
        return User.query.get(user_id)

    @staticmethod
    def change_password(user: User, new_password: str):
        """Change user password"""
        user.hashed_password = Security.hash_password(new_password)
        user.updated_at = datetime.utcnow()
        db.session.commit()