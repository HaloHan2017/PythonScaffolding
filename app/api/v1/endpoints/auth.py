"""Authentication endpoints"""
from datetime import datetime, timedelta
from flask import request
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
    get_jwt
)

from app.core.security import Security
from app.services.auth_service import AuthService
from app.api.v1.schemas.auth import (
    LoginSchema, TokenSchema, RefreshTokenSchema, ChangePasswordSchema
)

# Create namespace
auth_ns = Namespace("auth", description="Authentication operations")

# Models for documentation
login_model = auth_ns.model("Login", {
    "username": fields.String(required=True, description="Username"),
    "password": fields.String(required=True, description="Password")
})

token_model = auth_ns.model("Token", {
    "access_token": fields.String(description="Access token"),
    "refresh_token": fields.String(description="Refresh token"),
    "token_type": fields.String(description="Token type"),
    "expires_in": fields.Integer(description="Expiration in seconds")
})

refresh_model = auth_ns.model("Refresh", {
    "refresh_token": fields.String(required=True, description="Refresh token")
})

change_password_model = auth_ns.model("ChangePassword", {
    "current_password": fields.String(required=True, description="Current password"),
    "new_password": fields.String(required=True, description="New password")
})

logout_model = auth_ns.model("Logout", {
    "message": fields.String(description="Logout message")
})


@auth_ns.route("/login")
class Login(Resource):
    """User login"""

    @auth_ns.doc("user_login")
    @auth_ns.expect(login_model)
    @auth_ns.marshal_with(token_model)
    def post(self):
        """Login user and return tokens"""
        data = request.get_json()

        # Validate input
        schema = LoginSchema()
        errors = schema.validate(data)
        if errors:
            return {"errors": errors}, 400

        # Authenticate user
        username = data.get("username")
        password = data.get("password")

        user = AuthService.authenticate_user(username, password)
        if not user:
            return {"message": "Invalid credentials"}, 401

        # Update last login
        user.last_login = datetime.utcnow()
        user.save()

        # Create tokens
        access_token = create_access_token(
            identity=str(user.id),
            additional_claims={"role": user.role.value}
        )
        refresh_token = create_refresh_token(identity=str(user.id))

        # Store tokens
        AuthService.store_tokens(user, access_token, refresh_token)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
            "expires_in": 1800  # 30 minutes
        }


@auth_ns.route("/refresh")
class RefreshToken(Resource):
    """Refresh access token"""

    @auth_ns.doc("refresh_token")
    @auth_ns.expect(refresh_model)
    @auth_ns.marshal_with(token_model)
    def post(self):
        """Refresh access token using refresh token"""
        data = request.get_json()

        # Validate input
        schema = RefreshTokenSchema()
        errors = schema.validate(data)
        if errors:
            return {"errors": errors}, 400

        refresh_token = data.get("refresh_token")

        # Verify refresh token
        user_id = AuthService.verify_refresh_token(refresh_token)
        if not user_id:
            return {"message": "Invalid refresh token"}, 401

        # Create new access token
        user = AuthService.get_user_by_id(user_id)
        if not user:
            return {"message": "User not found"}, 404

        access_token = create_access_token(
            identity=str(user.id),
            additional_claims={"role": user.role.value}
        )

        return {
            "access_token": access_token,
            "token_type": "bearer",
            "expires_in": 1800
        }


@auth_ns.route("/logout")
class Logout(Resource):
    """User logout"""

    @auth_ns.doc("user_logout", security="Bearer")
    @auth_ns.expect(logout_model)
    @jwt_required()
    def post(self):
        """Logout user and revoke tokens"""
        jti = get_jwt()["jti"]
        AuthService.revoke_token(jti)

        return {"message": "Successfully logged out"}, 200


@auth_ns.route("/change-password")
class ChangePassword(Resource):
    """Change user password"""

    @auth_ns.doc("change_password", security="Bearer")
    @auth_ns.expect(change_password_model)
    @jwt_required()
    def post(self):
        """Change user password"""
        data = request.get_json()

        # Validate input
        schema = ChangePasswordSchema()
        errors = schema.validate(data)
        if errors:
            return {"errors": errors}, 400

        user_id = get_jwt_identity()
        current_password = data.get("current_password")
        new_password = data.get("new_password")

        # Verify current password
        user = AuthService.get_user_by_id(user_id)
        if not user:
            return {"message": "User not found"}, 404

        if not Security.verify_password(current_password, user.hashed_password):
            return {"message": "Current password is incorrect"}, 400

        # Update password
        AuthService.change_password(user, new_password)

        return {"message": "Password changed successfully"}, 200


@auth_ns.route("/me")
class CurrentUser(Resource):
    """Get current user information"""

    @auth_ns.doc("get_current_user", security="Bearer")
    @jwt_required()
    def get(self):
        """Get current authenticated user"""
        user_id = get_jwt_identity()
        user = AuthService.get_user_by_id(user_id)

        if not user:
            return {"message": "User not found"}, 404

        return user.to_dict(), 200