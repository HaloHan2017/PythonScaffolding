"""Custom exceptions for the application"""


class APIException(Exception):
    """Base API exception"""

    def __init__(
        self,
        message: str = "An error occurred",
        status_code: int = 500,
        payload: dict | None = None,
    ):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.payload = payload or {}

    def to_dict(self):
        """Convert exception to dictionary"""
        rv = dict(self.payload)
        rv["error"] = self.__class__.__name__
        rv["message"] = self.message
        return rv


class ValidationError(APIException):
    """Validation error exception"""

    def __init__(self, message: str = "Validation failed", payload: dict | None = None):
        super().__init__(message=message, status_code=400, payload=payload)


class AuthenticationError(APIException):
    """Authentication error exception"""

    def __init__(
        self, message: str = "Authentication failed", payload: dict | None = None
    ):
        super().__init__(message=message, status_code=401, payload=payload)


class AuthorizationError(APIException):
    """Authorization error exception"""

    def __init__(self, message: str = "Permission denied", payload: dict | None = None):
        super().__init__(message=message, status_code=403, payload=payload)


class NotFoundError(APIException):
    """Resource not found exception"""

    def __init__(
        self, message: str = "Resource not found", payload: dict | None = None
    ):
        super().__init__(message=message, status_code=404, payload=payload)


class ConflictError(APIException):
    """Resource conflict exception"""

    def __init__(self, message: str = "Resource conflict", payload: dict | None = None):
        super().__init__(message=message, status_code=409, payload=payload)


class ServiceUnavailableError(APIException):
    """Service unavailable exception"""

    def __init__(
        self, message: str = "Service unavailable", payload: dict | None = None
    ):
        super().__init__(message=message, status_code=503, payload=payload)
