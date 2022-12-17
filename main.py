# Coffee Machine
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def are_resources_sufficient(order_ingredients):
    """Returns true if there are enough ingredients to make the drink"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there isn't enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total amount from the coins entered."""
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


def is_transaction_successful(money_entered, drink_cost):
    """Return True if transaction is successful, of False if funds are insufficient."""
    if money_entered >= drink_cost:
        change = round(money_entered - drink_cost, 2)
        print(f"Here is ${change} in change.\n")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.\n")
        return False


def make_coffee(drink_name, drink_ingredients):
    """Deduct the proper ingredients from resources"""
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {drink_name}.☕\n")


power_on = True

while power_on:
    command = input("What would you like? (espresso-$1.50/latte-$2.50/cappuccino-$3.00): ").lower()
    if command == "off":
        power_on = False
    elif command == "report":
        print(f"\nWater: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}\n")
    else:
        drink = MENU[command]
        if are_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(command, drink["ingredients"])
