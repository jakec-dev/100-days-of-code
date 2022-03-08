MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
balance = 0

def insert_coins():
    """Promprt user to add coins. Return total"""
    print("Please insert coins.")
    coins = {}
    coins["25c"] = int(input("How many 25c coins?: "))
    coins["10c"] = int(input("How many 10c coins?: "))
    coins["5c"] = int(input("How many 5c coins?: "))
    coins["1c"] = int(input("How many 1c coins?: "))
    return coins["25c"] * 0.25 + coins["10c"] * 0.10 + coins["5c"] * 0.05 + coins["1c"] * 0.01

def adjust_resources(item, resources_balance):
    ingredients_required = MENU[item]["ingredients"]
    resources_remaining = resources_balance
    for ingredient in resources:
        if ingredient in ingredients_required:
            resources_remaining[ingredient] = resources_balance[ingredient] - ingredients_required[ingredient]
    return resources_remaining 

def check_availability(item_selected, r_balance):
    insufficient_ingredients = []
    resources_remaining_after = adjust_resources(item_selected, r_balance)
    for i in resources_remaining_after:
        if resources_remaining_after[i] < 0:
            insufficient_ingredients.append(i)
    return insufficient_ingredients

run_app = True
while run_app == True:
    selection = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if selection == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffe: {resources['coffee']}g")
        print(f"Money: ${format(balance, '.2f')}")
    elif selection == "off":
        run_app = False
    elif selection in MENU:
        amount_paid = insert_coins()
        price = MENU[selection]["cost"]
        change = amount_paid - price
        if change < 0:
            print("Not enough coins inserted. Please try again")
        else:
            insufficient_ingredients = check_availability(selection, resources)
            if len(insufficient_ingredients) > 0:
                print(f"Sorry, there is not enough {' and '.join(insufficient_ingredients)}")
            else:
                print(f"Here is your ${format(change, '.2f')} in change.")
                print(f"Here is your {selection}. Enjoy!")
                balance += price
    else:
        print("Wrong selection, try again.")