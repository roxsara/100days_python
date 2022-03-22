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

def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = pennies * 0.01 + nickles * 0.05 + dimes * 0.1 + quarters * 0.25
    return total

def enough_resources(order_ingredient):
    """Returns true if order can be processed and false if an ingredient is missing"""
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def is_transaction_successful(money_received, drink_cost):
    """Return True if payment is accepted, False is money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is {change} in change.")
        global profit
        profit += drink_cost

        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")

profit = 0
on = True

while on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {profit}")
    else:
        drink = MENU[choice]
        if enough_resources((drink["ingredients"])):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

