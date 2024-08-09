from tests.conftest import *

from src.api.models.product import Product
from src.api.models.portion import Portion
from src.api.models.unit import Unit
from tests.data import data_product_rice, data_unit_gr


def test_portion_creation():
    product = Product(**data_product_rice)
    unit_gr = Unit(**data_unit_gr)
    portion = Portion(product=product, unit=unit_gr, value=60)
    assert portion.value == 60
    assert portion.product.title == data_product_rice.get("title")


@pytest.mark.usefixtures("filled_session")
class TestPortion:

    def test_portion_category(self, filled_session):
        rice: Product = (
            filled_session.query(Product)
            .filter(Product.title == data_product_rice.get("title"))
            .first()
        )
        portion = (
            filled_session.query(Portion).filter(Portion.product_id == rice.id).first()
        )
        assert portion.product_category == rice.product_category
        assert portion.product_category_id == rice.product_category_id
