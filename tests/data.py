from __future__ import annotations

import datetime

data_user_alice = {
    "first_name": "Alice",
    "username": "Alice2000",
    "email": "alice@model.com",
    "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$vWYJlAvd1l6CrETvjGZqUw$O24OEcreETZQK4YYCPBB8+dms8pqvSyOx9C+Ac+8LOs"  # "password2000"
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

data_meal_breakfast = {
    "title": "Breakfast Meal",
    "description": "Breakfast Meal with different dishes",
}

data_mealtime_breakfast = {
    "title": "Breakfast Mealtime",
    "description": "Breakfast Mealtime with different meals and datetime",
}

data_mealtime_type_breakfast = {
    "title": "Breakfast Mealtime Type",
    "description": "Breakfast Mealtime Type with different mealtimes",
}

data_meal_dinner = {
    "title": "Dinner Meal",
    "description": "Dinner Meal with different dishes",
}

data_mealtime_dinner = {
    "title": "Dinner Mealtime",
    "description": "Dinner Mealtime with different meals and datetime",
}

data_mealtime_type_dinner = {
    "title": "Dinner Mealtime Type",
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
