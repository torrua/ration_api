from __future__ import annotations

from functools import wraps

from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import declarative_mixin, declared_attr


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
