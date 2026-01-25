"""Helper functions"""
import re
from typing import Any, Dict, List
from datetime import datetime, date


class Helpers:
    """Collection of helper functions"""

    @staticmethod
    def camel_to_snake(name: str) -> str:
        """Convert camelCase to snake_case"""
        name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()

    @staticmethod
    def snake_to_camel(name: str) -> str:
        """Convert snake_case to camelCase"""
        components = name.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])

    @staticmethod
    def format_datetime(value: datetime) -> str:
        """Format datetime to ISO format"""
        if value:
            return value.isoformat()
        return None

    @staticmethod
    def generate_pagination_metadata(total: int, page: int, per_page: int) -> Dict:
        """Generate pagination metadata"""
        total_pages = (total + per_page - 1) // per_page

        return {
            "total": total,
            "page": page,
            "per_page": per_page,
            "total_pages": total_pages,
            "has_next": page < total_pages,
            "has_prev": page > 1
        }

    @staticmethod
    def remove_none_values(data: Dict) -> Dict:
        """Remove None values from dictionary"""
        return {k: v for k, v in data.items() if v is not None}

    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate email format"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    @staticmethod
    def validate_phone(phone: str) -> bool:
        """Validate phone number format"""
        pattern = r'^\+?1?\d{9,15}$'
        return re.match(pattern, phone) is not None