from tests.conftest import *

from src.api.models.product import Product
from src.api.models.portion import Portion
from src.api.models.unit import Unit
from tests.data import rice_data, gr_data


def test_portion_creation():
    product = Product(**rice_data)
    unit_gr = Unit(**gr_data)
    portion = Portion(product=product, unit=unit_gr, value=60)
    assert portion.value == 60
    assert portion.product.name == rice_data.get("name")


@pytest.mark.usefixtures("filled_session")
class TestPortion:

    def test_portion_category(self, filled_session):
        rice: Product = (
            filled_session.query(Product)
            .filter(Product.name == rice_data.get("name"))
            .first()
        )
        portion = (
            filled_session.query(Portion).filter(Portion.product_id == rice.id).first()
        )
        assert portion.product_category == rice.product_category
        assert portion.product_category_id == rice.product_category_id

    def test_portion_title(self, filled_session):
        rice: Product = (
            filled_session.query(Product)
            .filter(Product.name == rice_data.get("name"))
            .first()
        )
        portion = (
            filled_session.query(Portion).filter(Portion.product_id == rice.id).first()
        )
        assert portion.title == f"{rice.name} - 60.0 {gr_data.get('name')}"
