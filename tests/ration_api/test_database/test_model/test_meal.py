from tests.conftest import *

from tests.data import (
    dinner_meal_data,
)


def test_meal_creation():
    meal = Meal(**dinner_meal_data)
    assert meal.title == dinner_meal_data.get("title")
    assert meal.description == dinner_meal_data.get("description")


@pytest.mark.usefixtures("filled_session")
class TestMeal:

    @staticmethod
    def meal(filled_session):
        return (
            filled_session.query(Meal)
            .filter(Meal.title == dinner_meal_data.get("title"))
            .first()
        )

    def test_meal_portions(self, filled_session):
        assert len(self.meal(filled_session).portions) == 5

    def test_meal_protein(self, filled_session):
        assert self.meal(filled_session).protein == 25.55

    def test_meal_carbohydrates(self, filled_session):
        assert self.meal(filled_session).carbohydrates == 102.47

    def test_meal_fat(self, filled_session):
        assert self.meal(filled_session).fat == 25.96

    def test_meal_calories(self, filled_session):
        assert self.meal(filled_session).calories == 732.25

    def test_meal_dishes(self, filled_session):
        assert len(self.meal(filled_session).dishes) == 2

    def test_meal_weight(self, filled_session):
        assert self.meal(filled_session).weight == 415.0
