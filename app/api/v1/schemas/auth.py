"""Authentication schemas"""
from marshmallow import Schema, fields, validate


class LoginSchema(Schema):
    """Schema for user login"""

    username = fields.Str(required=True)
    password = fields.Str(required=True)


class TokenSchema(Schema):
    """Schema for token response"""

    access_token = fields.Str(required=True)
    refresh_token = fields.Str(required=True)
    token_type = fields.Str(default="bearer")
    expires_in = fields.Int()


class RefreshTokenSchema(Schema):
    """Schema for token refresh"""

    refresh_token = fields.Str(required=True)


class ChangePasswordSchema(Schema):
    """Schema for password change"""

    current_password = fields.Str(required=True)
    new_password = fields.Str(
        required=True,
        validate=[
            validate.Length(min=8),
            validate.Regexp(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)')
        ]
    )