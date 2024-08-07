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
    fruits_product_category_data,
    meat_product_category_data,
    egg_data,
    sausage_data,
    dish_eggs_and_sausages_data,
    breakfast_meal_data,
    cereal_product_category_data,
    rice_data,
    gr_data,
    alice_data,
    dish_rice_with_lamb_oil_data,
    dinner_meal_data,
    lamb_data,
    first_trip_data,
    sunflower_oil_data,
    apple_data,
    ml_data,
    dish_apple_and_crackers_data,
    cracker_data,
    dinner_mealtime_data,
    dinner_mealtime_type_data,
    breakfast_mealtime_data,
    breakfast_mealtime_type_data,
    child_participant_data,
    adult_man_participant_data,
    adult_woman_participant_data,
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
    user = User(**alice_data)
    session_.add(user)
    session_.commit()
    unit_gr = Unit(**gr_data, user=user)
    unit_ml = Unit(**ml_data, user=user)
    session_.add_all([unit_gr, unit_ml])
    session_.commit()
    product_category_fruits = ProductCategory(**fruits_product_category_data, user=user)
    product_category_meat = ProductCategory(**meat_product_category_data, user=user)
    product_category_cereal = ProductCategory(**cereal_product_category_data, user=user)
    session_.add_all(
        [product_category_fruits, product_category_meat, product_category_cereal]
    )
    session_.commit()
    product_rice = Product(
        **rice_data,
        product_category=product_category_cereal,
        user=user,
    )
    product_lamb = Product(
        **lamb_data, product_category=product_category_meat, user=user
    )
    product_sunflower_oil = Product(**sunflower_oil_data, user=user)
    product_apple = Product(
        **apple_data, user=user, product_category=product_category_fruits
    )
    product_cracker = Product(**cracker_data, user=user)
    product_eggs = Product(**egg_data, user=user)
    product_sausages = Product(**sausage_data, user=user)
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
    dish_rice_with_lamb_oil = Dish(**dish_rice_with_lamb_oil_data, user=user)
    dish_apple_and_crackers = Dish(**dish_apple_and_crackers_data, user=user)
    dish_eggs_and_sausages = Dish(**dish_eggs_and_sausages_data, user=user)
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
    meal_dinner = Meal(**dinner_meal_data, user=user)
    meal_dinner_dishes = [dish_rice_with_lamb_oil, dish_apple_and_crackers]
    meal_dinner.dishes.extend(meal_dinner_dishes)
    mealtime_type_dinner = MealtimeType(**dinner_mealtime_type_data, user=user)
    mealtime_type_breakfast = MealtimeType(**breakfast_mealtime_type_data, user=user)
    session_.add_all([mealtime_type_dinner, mealtime_type_breakfast])
    mealtime_dinner = Mealtime(
        **dinner_mealtime_data,
        meal=meal_dinner,
        mealtime_type=mealtime_type_dinner,
    )
    portion_eggs = Portion(title="eggs", product=product_eggs, value=60, unit=unit_gr)
    portion_sausages = Portion(title="sausages", product=product_sausages, value=100, unit=unit_gr)
    dish_eggs_and_sausages_portions = [portion_eggs, portion_sausages]
    dish_eggs_and_sausages.portions.extend(dish_eggs_and_sausages_portions)
    meal_breakfast = Meal(**breakfast_meal_data, user=user)
    meal_breakfast.dishes.append(dish_eggs_and_sausages)
    mealtime_breakfast = Mealtime(
        **breakfast_mealtime_data,
        meal=meal_breakfast,
        mealtime_type=mealtime_type_breakfast,
    )
    participant_adult_man = Participant(**adult_man_participant_data, user=user)
    participant_adult_woman = Participant(**adult_woman_participant_data, user=user)
    participant_child = Participant(**child_participant_data, user=user)
    participants = [participant_adult_man, participant_adult_woman, participant_child]
    session_.add_all(participants)
    trip_first = Trip(**first_trip_data, user=user)
    trip_first_mealtimes = [mealtime_breakfast, mealtime_dinner]
    trip_first.mealtimes.extend(trip_first_mealtimes)
    trip_first.participants.extend(participants)
    session_.add(trip_first)
    session_.commit()
