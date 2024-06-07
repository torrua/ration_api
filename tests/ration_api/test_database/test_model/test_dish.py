from tests.conftest import *

from tests.data import (
    dish_rice_with_lamb_oil_data,
    dinner_meal_data,
)


def test_dish_creation():
    dish = Dish(**dish_rice_with_lamb_oil_data)
    assert dish.title == dish_rice_with_lamb_oil_data.get("title")
    assert dish.description == dish_rice_with_lamb_oil_data.get("description")


@pytest.mark.usefixtures("filled_session")
class TestDish:

    @staticmethod
    def dish(filled_session):
        return (
            filled_session.query(Dish)
            .filter(Dish.title == dish_rice_with_lamb_oil_data.get("title"))
            .first()
        )

    def test_dish_portions(self, filled_session):
        assert len(self.dish(filled_session).relationship_portions.all()) == 3

    def test_dish_meals(self, filled_session):
        assert self.dish(filled_session).relationship_meals[0].title == dinner_meal_data.get("title")

    def test_dish_calories(self, filled_session):
        assert self.dish(filled_session).calories == sum(
            [p.calories for p in self.dish(filled_session).relationship_portions]
        )

    def test_dish_carbohydrates(self, filled_session):
        assert self.dish(filled_session).carbohydrates == sum(
            [p.carbohydrates for p in self.dish(filled_session).relationship_portions]
        )

    def test_dish_fat(self, filled_session):
        assert self.dish(filled_session).fat == sum(
            [p.fat for p in self.dish(filled_session).relationship_portions]
        )

    def test_dish_protein(self, filled_session):
        assert self.dish(filled_session).protein == sum(
            [p.protein for p in self.dish(filled_session).relationship_portions]
        )

    def test_dish_is_fixed(self, filled_session):
        assert not self.dish(filled_session).is_fixed
