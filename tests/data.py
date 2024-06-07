from __future__ import annotations

import datetime

alice_data = {
    "first_name": "Alice",
    "username": "Alice2000",
    "email": "alice@model.com",
    "hashed_password": "pass1",
}
bob_data = {
    "first_name": "Bob",
    "username": "Bob2",
    "email": "bob@model.com",
    "hashed_password": "pass2",
}

rice_data = {
    "name": "Kpyпa риcoвaя",
    "protein": 7,
    "fat": 0.6,
    "carbohydrates": 73.7,
    "calories": 323,
}
lamb_data = {
    "name": "Бapaнинa",
    "protein": 16.3,
    "fat": 15.3,
    "carbohydrates": 0,
    "calories": 203,
}
apple_data = {
    "name": "Яблoки",
    "protein": 0.4,
    "fat": 0,
    "carbohydrates": 11.3,
    "calories": 46,
}
egg_data = {
    "name": "Яйцо",
    "protein": 12.7,
    "fat": 10.9,
    "carbohydrates": 0.7,
    "calories": 157,
}
sausage_data = {
    "name": "Сосиска",
    "protein": 11,
    "fat": 23.9,
    "carbohydrates": 0.4,
    "calories": 261,
}

cracker_data = {
    "name": "Cyxapи cливoчныe",
    "protein": 8.5,
    "fat": 10.6,
    "carbohydrates": 71.3,
    "calories": 397,
}
sunflower_oil_data = {
    "name": "Масло подсолнечное",
    "protein": 0,
    "fat": 99.9,
    "carbohydrates": 0,
    "calories": 899,
}

fruits_product_category_data = {
    "title": "Fruits",
}
meat_product_category_data = {
    "title": "Meat",
}
cereal_product_category_data = {
    "title": "Cereal",
}
dish_rice_with_lamb_oil_data = {
    "title": "Lamb and Rice",
    "description": "Dish with lamb and rice",
}

dish_apple_and_crackers_data = {
    "title": "Apple and Crackers",
    "description": "Dish with apple and crackers",
}

dish_eggs_and_sausages_data = {
    "title": "Eggs and Sausages",
    "description": "Dish with eggs and sausages",
}

breakfast_meal_data = {
    "title": "Breakfast Meal",
    "description": "Breakfast Meal with different dishes",
}

breakfast_mealtime_data = {
    "title": "Breakfast Mealtime",
    "description": "Breakfast Mealtime with different meals and datetime",
}

breakfast_mealtime_type_data = {
    "title": "Breakfast Mealtime Type",
    "description": "Breakfast Mealtime Type with different mealtimes",
}

dinner_meal_data = {
    "title": "Dinner Meal",
    "description": "Dinner Meal with different dishes",
}

dinner_mealtime_data = {
    "title": "Dinner Mealtime",
    "description": "Dinner Mealtime with different meals and datetime",
}

dinner_mealtime_type_data = {
    "title": "Dinner Mealtime Type",
    "description": "Dinner Mealtime Type with different mealtimes",
}

empty_product_category_data = {
    "title": "Test Product Category",
    "description": "Product Category with different products",
}

first_trip_data = {
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

ml_data = {
    "name": "мл.",
}
gr_data = {
    "name": "гр.",
}
ea_data = {
    "name": "шт.",
}
child_participant_data = {
    "name": "Child Participant",
    "coefficient": 0.6,
}
adult_man_participant_data = {
    "name": "Adult Man Participant",
    "coefficient": 1,
}
adult_woman_participant_data = {
    "name": "Adult Woman Participant",
    "coefficient": 0.8,
}
