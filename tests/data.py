from __future__ import annotations

import datetime

data_user_alice = {
    "first_name": "Alice",
    "username": "Alice2000",
    "email": "alice@model.com",
    "hashed_password": (
        "$argon2id$v=19$m=65536,t=3,"
        "p=4$vWYJlAvd1l6CrETvjGZqUw$O24OEcreETZQK4YYCPBB8+dms8pqvSyOx9C+Ac+8LOs"
    )  # "password2000"
}

data_user_bob = {
    "first_name": "Bob",
    "username": "Bob2",
    "email": "bob@model.com",
    "hashed_password": "pass2",
}

data_product_rice = {
    "title": "Kpyпa риcoвaя",
    "protein": 7,
    "fat": 0.6,
    "carbohydrates": 73.7,
    "calories": 323,
}

data_product_buckwheat = {
    'title': 'Крупа гpeчнeвaя ядpицa',
    'protein': 12.6,
    'fat': 2.6,
    'carbohydrates': 68,
    'calories': 329,
}

data_product_canned_meat = {
    'title': 'Тушенка говяжья',
    'protein': 5.2,
    'fat': 19.5,
    'carbohydrates': 3.7,
    'calories': 211,
}

data_product_tomato = {
    "title": "Помидор",
    "protein": 1.1,
    "fat": 0.2,
    "carbohydrates": 3.8,
    "calories": 24,
}

data_product_onion = {
    "title": "Лук репчатый",
    "protein": 1.1,
    "fat": 0.1,
    "carbohydrates": 9,
    "calories": 40,
}

data_product_fine_ground_barley = {
    "title": "Крупа ячневая",
    "protein": 10.4,
    "fat": 1.3,
    "carbohydrates": 66.3,
    "calories": 324,
}

data_product_dried_apricots = {
    "title": "Курага",
    "protein": 5.2,
    "fat": 0.3,
    "carbohydrates": 51.0,
    "calories": 215,
}

data_product_lamb = {
    "title": "Бapaнинa",
    "protein": 16.3,
    "fat": 15.3,
    "carbohydrates": 0,
    "calories": 203,
}

data_product_apple = {
    "title": "Яблoки",
    "protein": 0.4,
    "fat": 0,
    "carbohydrates": 11.3,
    "calories": 46,
}

data_product_egg = {
    "title": "Яйцо",
    "protein": 12.7,
    "fat": 10.9,
    "carbohydrates": 0.7,
    "calories": 157,
}

data_product_tea = {
    "title": "Чай",
    "protein": 20,
    "fat": 5.1,
    "carbohydrates": 6.9,
    "calories": 151.8,
}

data_product_coffee = {
    "title": "Кофе",
    "protein": 13.9,
    "fat": 14.4,
    "carbohydrates": 4.1,
    "calories": 200.6,
}

data_product_cookie = {
    "title": "Печенье овсяное",
    "protein": 6.2,
    "fat": 18.1,
    "carbohydrates": 65.9,
    "calories": 450,
}

data_product_sugar = {
    "title": "Сахар",
    "protein": 0,
    "fat": 0,
    "carbohydrates": 100,
    "calories": 400,
}

data_product_sausage = {
    "title": "Сосиска",
    "protein": 11,
    "fat": 23.9,
    "carbohydrates": 0.4,
    "calories": 261,
}

data_product_cracker = {
    "title": "Cyxapи cливoчныe",
    "protein": 8.5,
    "fat": 10.6,
    "carbohydrates": 71.3,
    "calories": 397,
}

data_product_sunflower_oil = {
    "title": "Масло подсолнечное",
    "protein": 0,
    "fat": 99.9,
    "carbohydrates": 0,
    "calories": 899,
}

data_product_category_fruits = {
    "title": "Fruits",
}

data_product_category_meat = {
    "title": "Meat",
}

data_product_category_cereal = {
    "title": "Cereal",
}

data_product_category_drinks = {
    "title": "Drinks",
}

data_product_category_sweets = {
    "title": "Sweets",
}

data_product_category_vegetables = {
    "title": "Vegetables",
}

data_dish_rice_with_lamb_oil = {
    "title": "Lamb and Rice",
    "description": "Dish with lamb and rice",
}

data_dish_apple_and_crackers = {
    "title": "Apple and Crackers",
    "description": "Dish with apple and crackers",
}

data_dish_eggs_and_sausages = {
    "title": "Eggs and Sausages",
    "description": "Dish with eggs and sausages",
}

data_dish_tea_with_sugar = {
    "title": "Tea with sugar",
    "description": "Dish with tea and sugar",
}

data_dish_coffee_with_cookie = {
    "title": "Coffee with Cookie",
    "description": "Dish with coffee and cookie",
}

data_dish_fine_ground_barley_with_dried_apricots = {
    "title": "Fine-Ground Barley with Dried Apricots",
    "description": "Dish with fine-ground barley and dried apricots",
}

data_dish_buckwheat_with_canned_meat = {
    "title": "Buckwheat with Canned Meat",
    "description": "Dish with buckwheat and canned meat",
}

data_dish_tomato_and_onion_salad = {
    "title": "Tomato and Onion Salad",
    "description": "Dish with tomato and onion salad",
}

data_meal_breakfast_1 = {
    "title": "Breakfast Meal (Variant 1)",
    "description": "Breakfast Meal (1) with different dishes",
}

data_meal_breakfast_2 = {
    "title": "Breakfast Meal (Variant 2)",
    "description": "Breakfast Meal (2) with different dishes",
}

data_meal_breakfast_3 = {
    "title": "Breakfast Meal (Variant 3)",
    "description": "Breakfast Meal (3) with different dishes",
}

data_mealtime_breakfast_01 = {
    "title": "Breakfast Mealtime 01",
    "description": "Breakfast Mealtime with different meals and datetime",
    "scheduled_at": datetime.datetime.strptime(
        "2024-01-01 06:30:00",
        "%Y-%m-%d %H:%M:%S",
    )
}

data_mealtime_breakfast_02 = {
    "title": "Breakfast Mealtime 02",
    "description": "Breakfast Mealtime with different meals and datetime",
    "scheduled_at": datetime.datetime.strptime(
        "2024-01-02 07:30:00",
        "%Y-%m-%d %H:%M:%S",
    )
}

data_mealtime_breakfast_03 = {
    "title": "Breakfast Mealtime 03",
    "description": "Breakfast Mealtime with different meals and datetime",
    "scheduled_at": datetime.datetime.strptime(
        "2024-01-03 08:30:00",
        "%Y-%m-%d %H:%M:%S",
    )
}

data_meal_dinner_1 = {
    "title": "Dinner Meal 1",
    "description": "Dinner Meal with different dishes",
}

data_meal_dinner_2 = {
    "title": "Dinner Meal 2",
    "description": "Dinner Meal with different dishes",
}

data_meal_dinner_3 = {
    "title": "Dinner Meal 3",
    "description": "Dinner Meal with different dishes",
}

data_mealtime_dinner_01 = {
    "title": "Dinner Meal 1",
    "description": "Dinner Mealtime with different meals and datetime",
    "scheduled_at": datetime.datetime.strptime(
        "2024-01-01 14:30:00",
        "%Y-%m-%d %H:%M:%S",
    ),
}

data_mealtime_dinner_02 = {
    "title": "Dinner Meal 2",
    "description": "Dinner Mealtime with different meals and datetime",
    "scheduled_at": datetime.datetime.strptime(
        "2024-01-02 14:00:00",
        "%Y-%m-%d %H:%M:%S",
    ),
}

data_mealtime_dinner_03 = {
    "title": "Dinner Meal ",
    "description": "Dinner Mealtime with different meals and datetime",
    "scheduled_at": datetime.datetime.strptime(
        "2024-01-03 15:00:00",
        "%Y-%m-%d %H:%M:%S",
    ),
}

data_mealtime_type_breakfast = {
    "title": "Breakfast",
    "description": "Breakfast Mealtime Type with different mealtimes",
}

data_mealtime_type_dinner = {
    "title": "Dinner",
    "description": "Dinner Mealtime Type with different mealtimes",
}

data_trip_first = {
    "title": "First Trip",
    "description": "First Trip with different mealtimes",
    "started_at": datetime.datetime.strptime(
        "2024-01-01 00:00:00",
        "%Y-%m-%d %H:%M:%S",
    ),
    "ended_at": datetime.datetime.strptime(
        "2024-01-14 00:00:00",
        "%Y-%m-%d %H:%M:%S",
    ),
}

data_trip_second = {
    "title": "Second Trip",
    "description": "Second Trip with different mealtimes",
    "started_at": datetime.datetime.strptime(
        "2024-02-01 00:00:00",
        "%Y-%m-%d %H:%M:%S",
    ),
    "ended_at": datetime.datetime.strptime(
        "2024-02-07 00:00:00",
        "%Y-%m-%d %H:%M:%S",
    ),
}

data_unit_ml = {
    "title": "мл.",
    "ratio_gr": 1.0,
}

data_unit_gr = {
    "title": "гр.",
    "ratio_gr": 1.0,
}

data_unit_kg = {
    "title": "кг.",
    "ratio_gr": 1000.0,
}

data_unit_oz = {
    "title": "oz.",
    "ratio_gr": 28.3495,
}

data_participant_child = {
    "title": "Child Participant",
    "coefficient": 0.6,
}

data_participant_adult_man = {
    "title": "Adult Man Participant",
    "coefficient": 1,
}

data_participant_adult_woman = {
    "title": "Adult Woman Participant",
    "coefficient": 0.8,
}
