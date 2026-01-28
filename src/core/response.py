"""Standardized API response formatting"""

from typing import Any, Optional

from flask import Response, jsonify


def success_response(
    data: Any = None,
    message: str = "Success",
    status_code: int = 200,
    meta: Optional[dict] = None,
) -> tuple[Response, int]:
    response = {
        "success": True,
        "message": message,
        "data": data,
    }

    if meta:
        response["meta"] = meta

    return jsonify(response), status_code


def error_response(
    message: str = "An error occurred",
    status_code: int = 500,
    errors: Optional[dict | list] = None,
) -> tuple[Response, int]:
    response = {
        "success": False,
        "message": message,
    }

    if errors:
        response["errors"] = errors  # type: ignore

    return jsonify(response), status_code


def paginated_response(
    data: list[Any],
    page: int,
    page_size: int,
    total: int,
    message: str = "Success",
) -> tuple[Response, int]:
    total_pages = (total + page_size - 1) // page_size if page_size > 0 else 0

    meta = {
        "pagination": {
            "page": page,
            "page_size": page_size,
            "total": total,
            "total_pages": total_pages,
        }
    }

    return success_response(data=data, message=message, meta=meta)


def created_response(
    data: Any = None, message: str = "Resource created successfully"
) -> tuple[Response, int]:
    """Create a 201 Created response"""
    return success_response(data=data, message=message, status_code=201)


def no_content_response() -> tuple[Response, int]:
    """Create a 204 No Content response"""
    return jsonify({}), 204
