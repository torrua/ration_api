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

    def test_meal_portions(self, filled_session):
        meal = (
            filled_session.query(Meal)
            .filter(Meal.title == dinner_meal_data.get("title"))
            .first()
        )
        assert len(meal.portions) == 5
