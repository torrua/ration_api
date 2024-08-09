from tests.conftest import *


def test_create_user():
    user_alice = User(**data_user_alice)
    assert user_alice.email == data_user_alice.get("email")


def cascade_delete_test(session, model, user_factory):
    user_id = user_factory(session).id
    assert session.query(model).filter(model.user_id == user_id).count() > 0

    session.delete(user_factory(session))
    session.commit()
    assert session.query(model).filter(model.user_id == user_id).count() == 0


@pytest.mark.usefixtures("filled_session")
class TestCreateUser:

    @staticmethod
    def user(filled_session):
        return (
            filled_session.query(User)
            .filter(User.email == data_user_alice.get("email"))
            .first()
        )

    def test_str(self, filled_session):
        user = self.user(filled_session)
        assert user.first_name == "Alice"
        assert user.email == "alice@model.com"
        assert user.username == "Alice2000"
        assert user.hashed_password == "$argon2id$v=19$m=65536,t=3,p=4$vWYJlAvd1l6CrETvjGZqUw$O24OEcreETZQK4YYCPBB8+dms8pqvSyOx9C+Ac+8LOs"
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
            "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$vWYJlAvd1l6CrETvjGZqUw$O24OEcreETZQK4YYCPBB8+dms8pqvSyOx9C+Ac+8LOs",
            "username": "Alice2000",
            "is_active": True,
        }

    def test_delete(self, filled_session):
        filled_session.delete(self.user(filled_session))
        assert filled_session.query(User).filter(User.email == data_user_alice.get("email")).first() is None

    def test_products_cascade_delete(self, filled_session):
        cascade_delete_test(filled_session, Product, self.user)

    def test_portions_cascade_delete(self, filled_session):
        cascade_delete_test(filled_session, Portion, self.user)

    def test_dishes_cascade_delete(self, filled_session):
        cascade_delete_test(filled_session, Dish, self.user)

    def test_meals_cascade_delete(self, filled_session):
        cascade_delete_test(filled_session, Meal, self.user)

    def test_mealtimes_cascade_delete(self, filled_session):
        cascade_delete_test(filled_session, Mealtime, self.user)

    def test_mealtime_types_cascade_delete(self, filled_session):
        cascade_delete_test(filled_session, MealtimeType, self.user)

    def test_participants_cascade_delete(self, filled_session):
        cascade_delete_test(filled_session, Participant, self.user)

    def test_product_categories_cascade_delete(self, filled_session):
        cascade_delete_test(filled_session, ProductCategory, self.user)

    def test_units_cascade_delete(self, filled_session):
        cascade_delete_test(filled_session, Unit, self.user)

    def test_trips_cascade_delete(self, filled_session):
        cascade_delete_test(filled_session, Trip, self.user)
