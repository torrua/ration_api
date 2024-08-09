from tests.conftest import *
from tests.data import data_product_rice, data_product_category_cereal


def test_create_product_category():
    product_category = ProductCategory(**data_product_category_cereal)
    assert product_category.title == data_product_category_cereal.get("title")


@pytest.mark.usefixtures("filled_session")
class TestProduct:

    @staticmethod
    def product_category(filled_session):
        return (
            filled_session.query(ProductCategory)
            .filter(ProductCategory.title == data_product_category_cereal.get("title"))
            .first()
        )

    def test_cascade_delete_in_products(self, filled_session):
        product_category = self.product_category(filled_session)
        product = product_category.products[0]
        assert product.product_category_id == product_category.id
        assert product.product_category == product_category

        filled_session.delete(product_category)
        filled_session.commit()
        filled_session.refresh(product)
        assert product.product_category_id is None
        assert product.product_category is None
