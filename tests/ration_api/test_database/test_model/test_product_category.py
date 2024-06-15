from tests.conftest import *
from tests.data import rice_data, cereal_product_category_data


def test_create_product_category():
    product_category = ProductCategory(**cereal_product_category_data)
    assert product_category.title == cereal_product_category_data.get("title")


@pytest.mark.usefixtures("filled_session")
class TestProduct:

    @staticmethod
    def product_category(filled_session):
        return (
            filled_session.query(ProductCategory)
            .filter(ProductCategory.title == cereal_product_category_data.get("title"))
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
