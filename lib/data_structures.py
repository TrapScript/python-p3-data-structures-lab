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
    names = []
    for food in spicy_foods:
        names.append(food['name'])
    return names


    

def get_spiciest_foods(spicy_foods):
    sfoods = []
    for sfood in spicy_foods:
        if sfood['heat'] > 5:
            sfoods.append(food)
        return sfoods

def print_spicy_foods(spicy_foods):
    for fud in spicy_foods:
        heat_level = "🌶" * food['heat_level']
        print(f"{fud['name']} ({fud['cuisine']}) | Heat Level: {heat_level}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
        return None

def print_spiciest_foods(spicy_foods):
    spiciest_food = []
    for food in spicy_foods:
        if food['heat_level'] >5:
            spiciest_food.append(food)

    def print_spicy_foods(spicy_foods):
        heat_level = "🌶" * food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")
    

def get_average_heat_level(spicy_foods):
    total_heat = sum(food['heat_level'] for food in spicy_foods)
    num_foods = len(spicy_foods)
    if num_food == 0:
        return 0
    average = total_heat / num_foods
    return average


def create_spicy_food(spicy_foods, spicy_food):
    pass
