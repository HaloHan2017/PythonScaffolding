"""User model using Peewee ORM"""

from peewee import BigAutoField, CharField, IntegerField

from src.core.database import BaseModel


class UserModel(BaseModel):
    """User model - maps to 'user' table in MySQL"""

    id = BigAutoField(primary_key=True)
    name = CharField(max_length=100, column_name="name")
    age = IntegerField(null=True)

    class Meta:
        table_name = "user"  # MySQL table name

    def __repr__(self):
        return f"<User {self.name}>"

    def to_dict(self) -> dict:
        """Convert model to dictionary"""
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
        }
