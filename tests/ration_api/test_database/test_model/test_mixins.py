from src.api.models.mixins import round_nutrition_value
import pytest


def test_round_nutrition_value_not_float():

    @round_nutrition_value
    def func():
        return "string"

    assert func() == "string"


def test_round_nutrition_value_float():

    @round_nutrition_value
    def func():
        return 1.2345

    assert func() == 1.23
