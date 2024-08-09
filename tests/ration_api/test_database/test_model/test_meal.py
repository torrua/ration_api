from tests.conftest import *

from tests.data import (
    data_meal_dinner,
)


def test_meal_creation():
    meal = Meal(**data_meal_dinner)
    assert meal.title == data_meal_dinner.get("title")
    assert meal.description == data_meal_dinner.get("description")


@pytest.mark.usefixtures("filled_session")
class TestMeal:

    @staticmethod
    def meal(filled_session):
        return (
            filled_session.query(Meal)
            .filter(Meal.title == data_meal_dinner.get("title"))
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
