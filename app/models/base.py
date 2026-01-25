"""Base model for all database models"""
from datetime import datetime
from typing import Any
from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.declarative import as_declarative, declared_attr

from app.core.extensions import db


@as_declarative()
class Base:
    """Base model class"""

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow, nullable=False)

    @declared_attr
    def __tablename__(cls) -> str:
        """Generate table name from class name"""
        return cls.__name__.lower()

    def to_dict(self) -> dict:
        """Convert model instance to dictionary"""
        return {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
        }

    def update(self, **kwargs) -> None:
        """Update model instance with given attributes"""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)