"""
Initial common functions for Model Classes
"""

from __future__ import annotations

from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr

from src.api.models.utils import camel_to_snake


class Base(DeclarativeBase):
    """
    Init class for common methods
    """

    __abstract__ = True
    """
    A class attribute that indicates that this class is an abstract base 
    class. When set to True, this class won't be mapped to any database 
    table. Instead, it serves as a base for other classes which will be 
    mapped to tables.
    """

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    """
    A class attribute mapped to a column in the database table. It serves as 
    the primary key for the table.

    :type: int
    """

    created_at: Mapped[datetime] = mapped_column(default=datetime.now())
    """
    A class attribute mapped to a column in the database table. It represents 
    the timestamp when a row is created. The default value is the current 
    timestamp, and it can't be null.

    :type: datetime
    """

    updated_at: Mapped[datetime | None] = mapped_column(
        onupdate=func.now()  # pylint: disable=E1102
    )
    """
    A class attribute mapped to a column in the database table. It represents 
    the timestamp when a row is last updated. Whenever the row is updated, 
    this timestamp is automatically set to the current time. It can be ``null`` 
    if the row has never been updated.

    :type: datetime
    """

    @declared_attr
    def __tablename__(self):
        return camel_to_snake(self.__name__)

    def __repr__(self):
        """
        Special method that returns a string representation of the object.
        It forms the string by joining key-value pairs of the object's attributes,
        excluding keys that start with "_" and keys that are "created_at", "updated_at" or "id".
        The key-value pairs are sorted before joining.

        Returns:
            str: A string representation of the object in the format:
                 "ClassName(key1=value1, key2=value2, ...)".
        """
        obj_str = ", ".join(
            sorted(
                [
                    f"{k}={v!r}"
                    for k, v in self.__dict__.items()
                    if self.check_attribute(k) and v
                ]
            )
        )
        return f"{self.__class__.__name__}({obj_str})"

    @staticmethod
    def check_attribute(attr_name: str) -> bool:
        return not attr_name.startswith("_") and attr_name not in [
            "created_at",
            "updated_at",
            "id",
        ]

    @classmethod
    def attributes_all(cls) -> set[str]:
        return set(cls.__mapper__.attrs.keys())

    @classmethod
    def attributes_basic(cls) -> set[str]:
        return set(cls.attributes_all() - cls.relationships())

    @classmethod
    def attributes_extended(cls) -> set[str]:
        return set(cls.attributes_all() - cls.foreign_keys())

    @classmethod
    def relationships(cls) -> set[str]:
        return set(cls.__mapper__.relationships.keys())

    @classmethod
    def foreign_keys(cls) -> set[str]:
        return set(cls.attributes_all() - cls.relationships() - cls.non_foreign_keys())

    @classmethod
    def non_foreign_keys(cls) -> set[str]:
        return {c.name for c in cls.__mapper__.columns if not c.foreign_keys}

    def as_dict(self) -> dict:
        return {
            attr: getattr(self, attr)
            for attr in self.attributes_basic()
            if self.check_attribute(attr) and getattr(self, attr)
        }
