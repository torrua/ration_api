from tests.conftest import *

from tests.data import (
    data_meal_dinner_1,
    data_mealtime_dinner_01,
    data_mealtime_type_dinner,
)


def test_mealtime_creation():
    meal = Meal(**data_meal_dinner_1)
    mealtime_type = MealtimeType(**data_mealtime_type_dinner)
    mealtime = Mealtime(**data_mealtime_dinner_01, meal=meal, mealtime_type=mealtime_type)
    assert mealtime.title == data_mealtime_dinner_01.get("title")
    assert mealtime.description == data_mealtime_dinner_01.get("description")


@pytest.mark.usefixtures("filled_session")
class TestMealtime:

    def test_mealtime_type(self, filled_session):
        mealtime = (
            filled_session.query(Mealtime)
            .filter(Mealtime.title == data_mealtime_dinner_01.get("title"))
            .first()
        )
        assert mealtime.mealtime_type.description == data_mealtime_type_dinner.get(
            "description"
        )

    @staticmethod
    def mealtime(filled_session):
        return (
            filled_session.query(Mealtime)
            .filter(Mealtime.title == data_mealtime_dinner_01.get("title"))
            .first()
        )

    def test_mealtime_scheduled_at(self, filled_session):
        assert self.mealtime(filled_session).scheduled_at.strftime(
            "%Y-%m-%d %H:%M:%S"
        ) == data_mealtime_dinner_01.get("scheduled_at").strftime("%Y-%m-%d %H:%M:%S")

    def test_mealtime_default_title(self, filled_session):
        assert self.mealtime(filled_session).default_title == 'Dinner 2024-01-01: Dinner Meal 1'  # TODO Refactor

    def test_mealtime_portions(self, filled_session):
        assert len(self.mealtime(filled_session).portions) == 5

    def test_mealtime_protein(self, filled_session):
        assert self.mealtime(filled_session).protein == 73.62

    def test_mealtime_carbohydrates(self, filled_session):
        assert self.mealtime(filled_session).carbohydrates == 272.46

    def test_mealtime_fat(self, filled_session):
        assert self.mealtime(filled_session).fat == 74.7

    def test_mealtime_calories(self, filled_session):
        assert self.mealtime(filled_session).calories == 2022.45

    def test_mealtime_weight(self, filled_session):
        assert self.mealtime(filled_session).weight == 1095.0

    def test_mealtime_dishes(self, filled_session):
        assert len(self.mealtime(filled_session).dishes) == 2
