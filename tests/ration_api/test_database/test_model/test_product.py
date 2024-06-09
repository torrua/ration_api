from tests.conftest import *
from tests.data import rice_data


def test_create_product():
    product_rice = Product(**rice_data)
    assert product_rice.title == "# Kpyпa риcoвaя 7.0/0.6/73.7 (323.0)"


@pytest.mark.usefixtures("filled_session")
class TestProduct:

    @staticmethod
    def product(filled_session):
        return (
            filled_session.query(Product)
            .filter(Product.name == rice_data.get("name"))
            .first()
        )

    def test__repr__(self, filled_session):
        assert self.product(filled_session).__repr__() == (
            "Product(calories=323.0, "
            "carbohydrates=73.7, fat=0.6, "
            "name='Kpyпa риcoвaя', "
            "product_category=ProductCategory(title='Cereal', user_id=1), "
            "product_category_id=3, "
            "protein=7.0, user_id=1)"
        )

    def test__str__(self, filled_session):
        assert (
            str(self.product(filled_session)) == "#5 Kpyпa риcoвaя 7.0/0.6/73.7 (323.0)"
        )

    def test_title(self, filled_session):
        assert (
            self.product(filled_session).title
            == "#5 Kpyпa риcoвaя 7.0/0.6/73.7 (323.0)"
        )

    def test_user(self, filled_session):
        assert self.product(filled_session).user.first_name == "Alice"

    def test_portions(self, filled_session):
        assert len(self.product(filled_session).portions) == 1
