from tests.conftest import *


def test_create_user():
    user_alice = User(**alice_data)
    assert user_alice.email == alice_data.get("email")


@pytest.mark.usefixtures("filled_session")
class TestCreateUser:

    @staticmethod
    def user(filled_session):
        return (
            filled_session.query(User)
            .filter(User.email == alice_data.get("email"))
            .first()
        )

    def test_str(self, filled_session):
        user = self.user(filled_session)
        assert user.first_name == "Alice"
        assert user.email == "alice@model.com"
        assert user.username == "Alice2000"
        assert user.hashed_password == "pass1"
        assert user.last_name is None
        assert user.is_verified is False
        assert user.is_superuser is False
        assert user.is_active is True

    @staticmethod
    def test_attribute_all():
        assert User.attributes_all() == {
            "created_at",
            "email",
            "first_name",
            "hashed_password",
            "id",
            "is_active",
            "is_superuser",
            "is_verified",
            "last_name",
            "updated_at",
            "username",
            "dishes",
            "meals",
            "mealtime_types",
            "mealtimes",
            "participants",
            "portions",
            "product_categories",
            "products",
            "trips",
            "units",
        }

    @staticmethod
    def test_attribute_basic():
        assert User.attributes_basic() == {
            "hashed_password",
            "is_active",
            "first_name",
            "created_at",
            "updated_at",
            "last_name",
            "username",
            "is_verified",
            "is_superuser",
            "id",
            "email",
        }

    @staticmethod
    def test_attribute_extended():
        assert User.attributes_extended() == {
            "hashed_password",
            "is_active",
            "first_name",
            "created_at",
            "updated_at",
            "is_verified",
            "last_name",
            "username",
            "id",
            "email",
            "is_superuser",
            "mealtime_types",
            "participants",
            "mealtimes",
            "product_categories",
            "units",
            "meals",
            "products",
            "dishes",
            "portions",
            "trips",
        }

    def test_as_dict(self, filled_session):
        assert self.user(filled_session).as_dict() == {
            "email": "alice@model.com",
            "first_name": "Alice",
            "hashed_password": "pass1",
            "username": "Alice2000",
            "is_active": True,
        }
