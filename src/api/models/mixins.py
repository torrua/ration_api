from __future__ import annotations

from functools import wraps

from sqlalchemy import Column, ForeignKey, UniqueConstraint, String
from sqlalchemy.orm import declarative_mixin, declared_attr

from src.api.models.utils import camel_to_snake


class NutritionCalculableMixin:  # pylint: disable=R0903

    calories: float
    protein: float
    fat: float
    carbohydrates: float


@declarative_mixin
class UserIdTitleUCMixin:

    @declared_attr
    def user_id(self):
        return Column("user_id", ForeignKey("user.id"), nullable=False)

    @declared_attr
    def title(self):
        return Column("title", String, nullable=False)

    @declared_attr
    def description(self):
        """
        A class attribute mapped to a column in the database table. It represents
        a description of the object. It can be ``null``.
        """
        return Column("description", String, nullable=True)

    @declared_attr
    def __table_args__(self):
        return (
            UniqueConstraint(
                "user_id",
                "title",
                name=f"_{camel_to_snake(self.__name__)}_user_id_title_uc",
            ),
        )


class WeightCalculableMixin:  # pylint: disable=R0903

    weight: float


def round_nutrition_value(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, float):
            return round(result, 2)
        return result

    return wrapper
