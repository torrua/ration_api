from tests.conftest import *
from tests.data import data_product_rice


def test_create_product():
    product_rice = Product(**data_product_rice)
    assert product_rice.__str__() == "# Kpyпa риcoвaя 7.0/0.6/73.7 (323.0)"


@pytest.mark.usefixtures("filled_session")
class TestProduct:

    @staticmethod
    def product(filled_session):
        return (
            filled_session.query(Product)
            .filter(Product.title == data_product_rice.get("title"))
            .first()
        )

    def test__repr__(self, filled_session):
        assert self.product(filled_session).__repr__() == (
            "Product(calories=323.0, "
            "carbohydrates=73.7, fat=0.6, "
            "product_category=ProductCategory(title='Cereal', user_id=1), "
            "product_category_id=3, "
            "protein=7.0, "
            "title='Kpyпa риcoвaя', "
            "user_id=1)"
        )

    def test__str__(self, filled_session):
        assert (
            str(self.product(filled_session)) == "#5 Kpyпa риcoвaя 7.0/0.6/73.7 (323.0)"
        )

    def test_user(self, filled_session):
        assert self.product(filled_session).user.first_name == "Alice"

    def test_portions(self, filled_session):
        assert len(self.product(filled_session).portions) == 1

    def test_delete_product(self, filled_session):
        filled_session.delete(self.product(filled_session))
        assert self.product(filled_session) is None

    def test_cascade_delete_portion(self, filled_session):
        portion_id = self.product(filled_session).portions[0].id
        assert portion_id is not None
        filled_session.delete(self.product(filled_session).portions[0])
        assert filled_session.query(Portion).filter(Portion.id == portion_id).first() is None
