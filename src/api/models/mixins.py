from __future__ import annotations

from functools import wraps

from sqlalchemy import Column, ForeignKey, UniqueConstraint
from sqlalchemy.orm import declarative_mixin, declared_attr, Mapped


class NutritionCalculableMixin:

    calories: float
    protein: float
    fat: float
    carbohydrates: float


@declarative_mixin
class RefUserMixin:  # pylint: disable=R0903

    @declared_attr
    def user_id(self):
        return Column("user_id", ForeignKey("user.id"), nullable=False)


@declarative_mixin
class UserIdTitleUCMixin(RefUserMixin):  # pylint: disable=R0903

    @declared_attr
    def __table_args__(self):
        return (
            UniqueConstraint(
                "user_id",
                "title",
                name=f"_{self.__name__.lower()}_user_id_title_uc",
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
