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
    data_dish_coffee_with_cookie,
    data_dish_eggs_and_sausages,
    data_dish_fine_ground_barley_with_dried_apricots,
    data_dish_rice_with_lamb_oil,
    data_dish_tea_with_sugar,
    data_dish_buckwheat_with_canned_meat,
    data_dish_tomato_and_onion_salad,
    data_meal_breakfast_1,
    data_meal_breakfast_2,
    data_meal_breakfast_3,
    data_meal_dinner_1,
    data_meal_dinner_2,
    data_meal_dinner_3,
    data_mealtime_breakfast_01,
    data_mealtime_breakfast_02,
    data_mealtime_breakfast_03,
    data_mealtime_dinner_01,
    data_mealtime_dinner_02,
    data_mealtime_dinner_03,
    data_mealtime_type_breakfast,
    data_mealtime_type_dinner,
    data_participant_adult_man,
    data_participant_adult_woman,
    data_participant_child,
    data_product_apple,
    data_product_canned_meat,
    data_product_category_cereal,
    data_product_category_drinks,
    data_product_category_fruits,
    data_product_category_meat,
    data_product_category_sweets,
    data_product_category_vegetables,
    data_product_coffee,
    data_product_cookie,
    data_product_cracker,
    data_product_dried_apricots,
    data_product_egg,
    data_product_fine_ground_barley,
    data_product_lamb,
    data_product_onion,
    data_product_rice,
    data_product_sausage,
    data_product_sugar,
    data_product_sunflower_oil,
    data_product_tea,
    data_product_tomato,
    data_product_buckwheat,
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
    product_category_drinks = ProductCategory(**data_product_category_drinks, user=user)
    product_category_sweets = ProductCategory(**data_product_category_sweets, user=user)
    product_category_vegetables = ProductCategory(
        **data_product_category_vegetables, user=user
    )

    session_.add_all(
        [
            product_category_fruits,
            product_category_meat,
            product_category_cereal,
            product_category_drinks,
            product_category_sweets,
            product_category_vegetables,
        ]
    )
    session_.commit()

    product_rice = Product(
        **data_product_rice,
        product_category=product_category_cereal,
        user=user,
    )
    product_buckwheat = Product(
        **data_product_buckwheat, product_category=product_category_cereal, user=user
    )
    product_lamb = Product(
        **data_product_lamb, product_category=product_category_meat, user=user
    )
    product_canned_meat = Product(
        **data_product_canned_meat, product_category=product_category_meat, user=user
    )

    product_sunflower_oil = Product(**data_product_sunflower_oil, user=user)
    product_apple = Product(
        **data_product_apple, user=user, product_category=product_category_fruits
    )
    product_tomato = Product(
        **data_product_tomato, product_category=product_category_vegetables, user=user
    )
    product_onion = Product(
        **data_product_onion, product_category=product_category_vegetables, user=user
    )
    product_cracker = Product(**data_product_cracker, user=user)
    product_eggs = Product(**data_product_egg, user=user)
    product_sausages = Product(
        **data_product_sausage, product_category=product_category_meat, user=user
    )
    product_tea = Product(
        **data_product_tea, product_category=product_category_drinks, user=user
    )
    product_sugar = Product(
        **data_product_sugar, product_category=product_category_sweets, user=user
    )
    product_coffee = Product(
        **data_product_coffee, product_category=product_category_drinks, user=user
    )
    product_cookie = Product(
        **data_product_cookie, product_category=product_category_sweets, user=user
    )
    product_fine_ground_barley = Product(
        **data_product_fine_ground_barley,
        product_category=product_category_cereal,
        user=user,
    )
    product_dried_apricots = Product(
        **data_product_dried_apricots,
        product_category=product_category_sweets,
        user=user,
    )

    session_.add_all(
        [
            product_sausages,
            product_eggs,
            product_apple,
            product_cracker,
            product_rice,
            product_lamb,
            product_sunflower_oil,
            product_tea,
            product_sugar,
            product_coffee,
            product_cookie,
            product_fine_ground_barley,
            product_dried_apricots,
        ]
    )

    dish_rice_with_lamb_oil = Dish(**data_dish_rice_with_lamb_oil, user=user)
    dish_apple_and_crackers = Dish(**data_dish_apple_and_crackers, user=user)
    dish_eggs_and_sausages = Dish(**data_dish_eggs_and_sausages, user=user)
    dish_tea_with_sugar = Dish(**data_dish_tea_with_sugar, user=user)
    dish_coffee_with_cookie = Dish(**data_dish_coffee_with_cookie, user=user)
    dish_fine_ground_barley_with_dried_apricots = Dish(
        **data_dish_fine_ground_barley_with_dried_apricots, user=user
    )
    dish_buckwheat_with_canned_meat = Dish(
        **data_dish_buckwheat_with_canned_meat, user=user
    )
    dish_tomato_and_onion_salad = Dish(**data_dish_tomato_and_onion_salad, user=user)

    session_.add_all(
        [
            dish_rice_with_lamb_oil,
            dish_apple_and_crackers,
            dish_eggs_and_sausages,
            dish_tea_with_sugar,
            dish_coffee_with_cookie,
            dish_fine_ground_barley_with_dried_apricots,
        ]
    )

    portion_rice = Portion(
        title="rice", product=product_rice, value=60, unit=unit_gr, is_fixed=True
    )
    portion_canned_meat = Portion(
        title="canned_meat", product=product_canned_meat, value=100, unit=unit_gr
    )
    portion_buckwheat = Portion(
        title="buckwheat", product=product_buckwheat, value=70, unit=unit_gr
    )
    portion_tomato = Portion(
        title="tomato", product=product_tomato, value=100, unit=unit_gr
    )
    portion_onion = Portion(
        title="onion", product=product_onion, value=25, unit=unit_gr
    )
    portion_lamb = Portion(title="lamb", product=product_lamb, value=100, unit=unit_gr)
    portion_sunflower_oil = Portion(
        title="sunflower_oil", product=product_sunflower_oil, value=5, unit=unit_ml
    )
    portion_apple = Portion(
        title="apple", product=product_apple, value=200, unit=unit_gr
    )
    portion_cracker = Portion(
        title="cracker", product=product_cracker, value=50, unit=unit_gr
    )
    portion_eggs = Portion(title="eggs", product=product_eggs, value=60, unit=unit_gr)
    portion_sausages = Portion(
        title="sausages", product=product_sausages, value=100, unit=unit_gr
    )
    portion_tea = Portion(
        title="tea", product=product_tea, value=2, unit=unit_gr, is_fixed=True
    )
    portion_sugar = Portion(
        title="sugar", product=product_sugar, value=5, unit=unit_gr, is_fixed=True
    )

    portion_coffee = Portion(
        title="coffee", product=product_coffee, value=5, unit=unit_gr, is_fixed=True
    )
    portion_cookie = Portion(
        title="cookie", product=product_cookie, value=20, unit=unit_gr
    )
    portion_fine_ground_barley = Portion(
        title="fine_ground_barley",
        product=product_fine_ground_barley,
        value=60,
        unit=unit_gr,
    )
    portion_dried_apricots = Portion(
        title="dried_apricots", product=product_dried_apricots, value=30, unit=unit_gr
    )

    dish_rice_with_lamb_oil_portions = [
        portion_rice,
        portion_lamb,
        portion_sunflower_oil,
    ]
    dish_rice_with_lamb_oil.portions.extend(dish_rice_with_lamb_oil_portions)
    dish_apple_and_crackers_portions = [portion_apple, portion_cracker]
    dish_apple_and_crackers.portions.extend(dish_apple_and_crackers_portions)
    dish_eggs_and_sausages_portions = [portion_eggs, portion_sausages]
    dish_eggs_and_sausages.portions.extend(dish_eggs_and_sausages_portions)
    dish_tea_with_sugar_portions = [portion_tea, portion_sugar]
    dish_tea_with_sugar.portions.extend(dish_tea_with_sugar_portions)
    dish_coffee_with_cookie_portions = [portion_coffee, portion_cookie]
    dish_coffee_with_cookie.portions.extend(dish_coffee_with_cookie_portions)
    dish_fine_ground_barley_with_dried_apricots_portions = [
        portion_fine_ground_barley,
        portion_dried_apricots,
    ]
    dish_fine_ground_barley_with_dried_apricots.portions.extend(
        dish_fine_ground_barley_with_dried_apricots_portions
    )
    dish_tomato_and_onion_salad.portions.extend([portion_tomato, portion_onion])
    dish_buckwheat_with_canned_meat.portions.extend(
        [portion_buckwheat, portion_canned_meat]
    )

    mealtime_type_dinner = MealtimeType(**data_mealtime_type_dinner, user=user)
    mealtime_type_breakfast = MealtimeType(**data_mealtime_type_breakfast, user=user)
    session_.add_all([mealtime_type_dinner, mealtime_type_breakfast])

    meal_breakfast_1 = Meal(**data_meal_breakfast_1, user=user)
    meal_breakfast_1.dishes.extend([dish_tea_with_sugar, dish_eggs_and_sausages])
    mealtime_breakfast_01 = Mealtime(
        **data_mealtime_breakfast_01,
        meal=meal_breakfast_1,
        mealtime_type=mealtime_type_breakfast,
    )

    meal_breakfast_2 = Meal(**data_meal_breakfast_2, user=user)
    meal_breakfast_2.dishes.extend(
        [dish_tea_with_sugar, dish_fine_ground_barley_with_dried_apricots]
    )
    mealtime_breakfast_02 = Mealtime(
        **data_mealtime_breakfast_02,
        meal=meal_breakfast_2,
        mealtime_type=mealtime_type_breakfast,
    )

    meal_breakfast_3 = Meal(**data_meal_breakfast_3, user=user)
    meal_breakfast_3.dishes.extend([dish_coffee_with_cookie, dish_eggs_and_sausages])
    mealtime_breakfast_03 = Mealtime(
        **data_mealtime_breakfast_03,
        meal=meal_breakfast_3,
        mealtime_type=mealtime_type_breakfast,
    )

    meal_dinner_1 = Meal(**data_meal_dinner_1, user=user)
    meal_dinner_1.dishes.extend([dish_rice_with_lamb_oil, dish_apple_and_crackers])
    mealtime_dinner_01 = Mealtime(
        **data_mealtime_dinner_01,
        meal=meal_dinner_1,
        mealtime_type=mealtime_type_dinner,
    )

    meal_dinner_2 = Meal(**data_meal_dinner_2, user=user)
    meal_dinner_2.dishes.extend([dish_buckwheat_with_canned_meat, dish_tomato_and_onion_salad])
    mealtime_dinner_02 = Mealtime(
        **data_mealtime_dinner_02,
        meal=meal_dinner_2,
        mealtime_type=mealtime_type_dinner,
    )

    meal_dinner_3 = Meal(**data_meal_dinner_3, user=user)
    meal_dinner_3.dishes.extend([dish_rice_with_lamb_oil, dish_tomato_and_onion_salad])
    mealtime_dinner_03 = Mealtime(
        **data_mealtime_dinner_03,
        meal=meal_dinner_3,
        mealtime_type=mealtime_type_dinner,
    )

    participant_adult_man = Participant(**data_participant_adult_man, user=user)
    participant_adult_woman = Participant(**data_participant_adult_woman, user=user)
    participant_child = Participant(**data_participant_child, user=user)
    participants = [participant_adult_man, participant_adult_woman, participant_child]

    session_.add_all(participants)
    trip_first = Trip(**data_trip_first, user=user)
    trip_first_mealtimes = [
        mealtime_breakfast_01,
        mealtime_breakfast_02,
        mealtime_breakfast_03,
        mealtime_dinner_01,
        mealtime_dinner_02,
        mealtime_dinner_03,
    ]
    trip_first.mealtimes.extend(trip_first_mealtimes)
    trip_first.participants.extend(participants)
    session_.add(trip_first)
    session_.commit()
