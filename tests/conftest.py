import pytest
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import scoped_session, sessionmaker

from src.api.models import (
    Base,
    Dish,
    Meal,
    Mealtime,
    MealtimeType,
    Participant,
    Portion,
    Product,
    ProductCategory,
    Trip,
    Unit,
    User,
)
from tests.data import (
    data_dish_apple_and_crackers,
    data_dish_eggs_and_sausages,
    data_dish_rice_with_lamb_oil,

    data_meal_breakfast,
    data_meal_dinner,

    data_mealtime_breakfast,
    data_mealtime_dinner,

    data_mealtime_type_breakfast,
    data_mealtime_type_dinner,

    data_participant_adult_man,
    data_participant_adult_woman,
    data_participant_child,

    data_product_category_cereal,
    data_product_category_fruits,
    data_product_category_meat,

    data_product_apple,
    data_product_cracker,
    data_product_egg,
    data_product_lamb,
    data_product_rice,
    data_product_sausage,
    data_product_sunflower_oil,

    data_trip_first,

    data_unit_gr,
    data_unit_ml,

    data_user_alice,
)


@pytest.fixture(scope="function")
def db_engine() -> Engine:
    """yields a SQLAlchemy engine which is suppressed after the test session"""
    engine_: Engine = create_engine("sqlite:///:memory:", echo=False)
    Base.metadata.create_all(engine_)

    yield engine_

    Base.metadata.drop_all(engine_)
    engine_.dispose()


@pytest.fixture(scope="function")
def db_session_factory(db_engine):
    """returns a SQLAlchemy scoped session factory"""
    return scoped_session(sessionmaker(bind=db_engine, future=True))


@pytest.fixture(scope="function")
def filled_session(db_session_factory):
    """yields a SQLAlchemy connection which is rollbacked after the test"""
    session_ = db_session_factory()

    fill_db(session_)
    yield session_

    session_.rollback()
    session_.close()


def fill_db(session_):
    user = User(**data_user_alice)
    session_.add(user)
    session_.commit()
    unit_gr = Unit(**data_unit_gr, user=user)
    unit_ml = Unit(**data_unit_ml, user=user)
    session_.add_all([unit_gr, unit_ml])
    session_.commit()
    product_category_fruits = ProductCategory(**data_product_category_fruits, user=user)
    product_category_meat = ProductCategory(**data_product_category_meat, user=user)
    product_category_cereal = ProductCategory(**data_product_category_cereal, user=user)
    session_.add_all(
        [product_category_fruits, product_category_meat, product_category_cereal]
    )
    session_.commit()
    product_rice = Product(
        **data_product_rice,
        product_category=product_category_cereal,
        user=user,
    )
    product_lamb = Product(
        **data_product_lamb, product_category=product_category_meat, user=user
    )
    product_sunflower_oil = Product(**data_product_sunflower_oil, user=user)
    product_apple = Product(
        **data_product_apple, user=user, product_category=product_category_fruits
    )
    product_cracker = Product(**data_product_cracker, user=user)
    product_eggs = Product(**data_product_egg, user=user)
    product_sausages = Product(**data_product_sausage, user=user)
    session_.add_all(
        [
            product_sausages,
            product_eggs,
            product_apple,
            product_cracker,
            product_rice,
            product_lamb,
            product_sunflower_oil,
        ]
    )
    portion_rice = Portion(
        title="rice",
        product=product_rice,
        value=60,
        unit=unit_gr,
        is_fixed=True,
    )
    portion_lamb = Portion(
        title="lamb",
        product=product_lamb,
        value=100,
        unit=unit_gr,
    )
    portion_sunflower_oil = Portion(
        title="sunflower_oil",
        product=product_sunflower_oil,
        value=5,
        unit=unit_ml,
    )
    dish_rice_with_lamb_oil = Dish(**data_dish_rice_with_lamb_oil, user=user)
    dish_apple_and_crackers = Dish(**data_dish_apple_and_crackers, user=user)
    dish_eggs_and_sausages = Dish(**data_dish_eggs_and_sausages, user=user)
    session_.add_all(
        [dish_rice_with_lamb_oil, dish_apple_and_crackers, dish_eggs_and_sausages]
    )
    dish_rice_with_lamb_oil_portions = [
        portion_rice,
        portion_lamb,
        portion_sunflower_oil,
    ]
    dish_rice_with_lamb_oil.portions.extend(dish_rice_with_lamb_oil_portions)
    portion_apple = Portion(title="apple", product=product_apple, value=200, unit=unit_gr)
    portion_cracker = Portion(title="cracker", product=product_cracker, value=50, unit=unit_gr)
    dish_apple_and_crackers_portions = [portion_apple, portion_cracker]
    dish_apple_and_crackers.portions.extend(dish_apple_and_crackers_portions)
    meal_dinner = Meal(**data_meal_dinner, user=user)
    meal_dinner_dishes = [dish_rice_with_lamb_oil, dish_apple_and_crackers]
    meal_dinner.dishes.extend(meal_dinner_dishes)
    mealtime_type_dinner = MealtimeType(**data_mealtime_type_dinner, user=user)
    mealtime_type_breakfast = MealtimeType(**data_mealtime_type_breakfast, user=user)
    session_.add_all([mealtime_type_dinner, mealtime_type_breakfast])
    mealtime_dinner = Mealtime(
        **data_mealtime_dinner,
        meal=meal_dinner,
        mealtime_type=mealtime_type_dinner,
    )
    portion_eggs = Portion(title="eggs", product=product_eggs, value=60, unit=unit_gr)
    portion_sausages = Portion(title="sausages", product=product_sausages, value=100, unit=unit_gr)
    dish_eggs_and_sausages_portions = [portion_eggs, portion_sausages]
    dish_eggs_and_sausages.portions.extend(dish_eggs_and_sausages_portions)
    meal_breakfast = Meal(**data_meal_breakfast, user=user)
    meal_breakfast.dishes.append(dish_eggs_and_sausages)
    mealtime_breakfast = Mealtime(
        **data_mealtime_breakfast,
        meal=meal_breakfast,
        mealtime_type=mealtime_type_breakfast,
    )
    participant_adult_man = Participant(**data_participant_adult_man, user=user)
    participant_adult_woman = Participant(**data_participant_adult_woman, user=user)
    participant_child = Participant(**data_participant_child, user=user)
    participants = [participant_adult_man, participant_adult_woman, participant_child]
    session_.add_all(participants)
    trip_first = Trip(**data_trip_first, user=user)
    trip_first_mealtimes = [mealtime_breakfast, mealtime_dinner]
    trip_first.mealtimes.extend(trip_first_mealtimes)
    trip_first.participants.extend(participants)
    session_.add(trip_first)
    session_.commit()
