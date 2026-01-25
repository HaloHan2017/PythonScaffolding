"""User schemas"""
from marshmallow import Schema, fields, validate, post_load
import re

from app.models.user import UserRole


class UserCreateSchema(Schema):
    """Schema for user creation"""

    username = fields.Str(
        required=True,
        validate=[
            validate.Length(min=3, max=50),
            validate.Regexp(r'^[a-zA-Z0-9_]+$',
                            error="Username can only contain letters, numbers, and underscores")
        ]
    )

    email = fields.Email(required=True)

    password = fields.Str(
        required=True,
        validate=[
            validate.Length(min=8),
            validate.Regexp(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)',
                            error="Password must contain uppercase, lowercase and numbers")
        ]
    )

    full_name = fields.Str(validate=validate.Length(max=100))
    phone_number = fields.Str(validate=validate.Length(max=20))

    @post_load
    def normalize_username(self, data, **kwargs):
        """Normalize username to lowercase"""
        if 'username' in data:
            data['username'] = data['username'].lower()
        return data


class UserUpdateSchema(Schema):
    """Schema for user update"""

    full_name = fields.Str(validate=validate.Length(max=100))
    phone_number = fields.Str(validate=validate.Length(max=20))
    is_active = fields.Boolean()


class UserResponseSchema(Schema):
    """Schema for user response"""

    id = fields.Int()
    username = fields.Str()
    email = fields.Email()
    full_name = fields.Str()
    phone_number = fields.Str()
    role = fields.Str()
    is_active = fields.Boolean()
    is_verified = fields.Boolean()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_login = fields.DateTime()


class UserListSchema(Schema):
    """Schema for user list response"""

    users = fields.Nested(UserResponseSchema, many=True)
    total = fields.Int()
    page = fields.Int()
    per_page = fields.Int()
    total_pages = fields.Int()