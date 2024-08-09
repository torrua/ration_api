from tests.conftest import *

from tests.data import (
    data_dish_rice_with_lamb_oil,
    data_meal_dinner,
)


def test_dish_creation():
    dish = Dish(**data_dish_rice_with_lamb_oil)
    assert dish.title == data_dish_rice_with_lamb_oil.get("title")
    assert dish.description == data_dish_rice_with_lamb_oil.get("description")


@pytest.mark.usefixtures("filled_session")
class TestDish:

    @staticmethod
    def dish(filled_session):
        return (
            filled_session.query(Dish)
            .filter(Dish.title == data_dish_rice_with_lamb_oil.get("title"))
            .first()
        )

    def test_dish_portions(self, filled_session):
        assert len(self.dish(filled_session).portions) == 3

    def test_dish_meals(self, filled_session):
        assert self.dish(filled_session).meals[0].title == data_meal_dinner.get("title")

    def test_dish_calories(self, filled_session):
        assert self.dish(filled_session).calories == sum(
            [p.calories for p in self.dish(filled_session).portions]
        )

    def test_dish_carbohydrates(self, filled_session):
        assert self.dish(filled_session).carbohydrates == sum(
            [p.carbohydrates for p in self.dish(filled_session).portions]
        )

    def test_dish_fat(self, filled_session):
        assert self.dish(filled_session).fat == sum(
            [p.fat for p in self.dish(filled_session).portions]
        )

    def test_dish_protein(self, filled_session):
        assert self.dish(filled_session).protein == sum(
            [p.protein for p in self.dish(filled_session).portions]
        )

    def test_dish_weight(self, filled_session):
        assert self.dish(filled_session).weight == sum(
            [p.weight for p in self.dish(filled_session).portions]
        )

    def test_dish_is_fixed(self, filled_session):
        assert self.dish(filled_session).is_fixed
