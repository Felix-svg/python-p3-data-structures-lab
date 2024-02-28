spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    food_list = []
    for food in spicy_foods:
        foods = food["name"]
        food_list.append(foods)
    return food_list
    #return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    spicy_list = []
    for spiciest in spicy_foods:
        if spiciest["heat_level"] > 5:
            spicy_list.append(spiciest)
    return spicy_list

def print_spicy_foods(spicy_foods):
    for spicy_food in spicy_foods:
        print(f'{spicy_food["name"]} ({spicy_food["cuisine"]}) | Heat Level: {"🌶" * spicy_food["heat_level"]}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    spicy_list = []
    for spiciest in spicy_foods:
        if spiciest["heat_level"] > 5:
            spicy_list.append(spiciest)
            print(f'{spiciest["name"]} ({spiciest["cuisine"]}) | Heat Level: {"🌶" * spiciest["heat_level"]}') 

def get_average_heat_level(spicy_foods):
    total_heat_level = 0
    for spicy_food in spicy_foods:
        total_heat_level += spicy_food["heat_level"]
        
    average_heat_level = total_heat_level / len(spicy_foods)
    return average_heat_level

# spicy_food =  {
#         "name": "Matumbo",
#         "cuisine": "Kenyan",
#         "heat_level": 10,
#     }

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
#create_spicy_food(spicy_foods, spicy_food)