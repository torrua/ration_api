from tests.conftest import *

from tests.data import (
    dinner_meal_data,
    dinner_mealtime_data,
    dinner_mealtime_type_data,
)


def test_mealtime_creation():
    meal = Meal(**dinner_meal_data)
    mealtime_type = MealtimeType(**dinner_mealtime_type_data)
    mealtime = Mealtime(**dinner_mealtime_data, meal=meal, mealtime_type=mealtime_type)
    assert mealtime.title == dinner_mealtime_data.get("title")
    assert mealtime.description == dinner_mealtime_data.get("description")


@pytest.mark.usefixtures("filled_session")
class TestMealtime:

    def test_mealtime_type(self, filled_session):
        mealtime = (
            filled_session.query(Mealtime)
            .filter(Mealtime.title == dinner_mealtime_data.get("title"))
            .first()
        )
        assert mealtime.mealtime_type.description == dinner_mealtime_type_data.get(
            "description"
        )

    @staticmethod
    def mealtime(filled_session):
        return (
            filled_session.query(Mealtime)
            .filter(Mealtime.title == dinner_mealtime_data.get("title"))
            .first()
        )

    def test_mealtime_portions(self, filled_session):
        assert len(self.mealtime(filled_session).portions) == 5

    def test_mealtime_protein(self, filled_session):
        assert self.mealtime(filled_session).protein == 61.32

    def test_mealtime_carbohydrates(self, filled_session):
        assert self.mealtime(filled_session).carbohydrates == 245.93

    def test_mealtime_fat(self, filled_session):
        assert self.mealtime(filled_session).fat == 62.3

    def test_mealtime_calories(self, filled_session):
        assert self.mealtime(filled_session).calories == 1757.4

    def test_mealtime_weight(self, filled_session):
        assert self.mealtime(filled_session).weight == 996.0

    def test_mealtime_dishes(self, filled_session):
        assert len(self.mealtime(filled_session).dishes) == 2
