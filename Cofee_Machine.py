MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

RESOURCES = {
    "Water": 3000,
    "Milk": 2000,
    "Coffee": 1000,
    "Money": 0
}


def coffee_order(order_name):
    drink = MENU[order_name]

    water_needed = drink["ingredients"]["water"]
    milk_needed = drink["ingredients"]["milk"]
    coffee_needed = drink["ingredients"]["coffee"]
    cost = drink["cost"]

    if RESOURCES["Water"] < water_needed:
        print("Sorry, there is not enough water.")
        return False

    if RESOURCES["Milk"] < milk_needed:
        print("Sorry, there is not enough milk.")
        return False

    if RESOURCES["Coffee"] < coffee_needed:
        print("Sorry, there is not enough coffee.")
        return False

    RESOURCES["Water"] -= water_needed
    RESOURCES["Milk"] -= milk_needed
    RESOURCES["Coffee"] -= coffee_needed
    RESOURCES["Money"] += cost
    print(f"Here is your {order_name}. Enjoy!")
    return True


def coffee_machine():

    power_on = True

    while power_on:

        order_name = input(
            "What would you like? (espresso/latte/cappuccino): "
        ).lower()
        if order_name == "off":
            power_on = False
        elif order_name == "report":
            print(RESOURCES)
        elif order_name not in MENU:
            print("Please choose espresso, latte or cappuccino.")

        else:
            cost = MENU[order_name]["cost"]
            money_offered = 0
            quarters = 0.25
            dimes = 0.10
            nickles = 0.05
            pennies = 0.01

            quarters_offered = int(input("How many quarters? "))
            dimes_offered = int(input("How many dimes? "))
            nickles_offered = int(input("How many nickels? "))
            pennies_offered = int(input("How many pennies? "))

            money_offered += quarters_offered * quarters
            money_offered += dimes_offered * dimes
            money_offered += nickles_offered * nickles
            money_offered += pennies_offered * pennies

            # Not enough money
            if money_offered < cost:
                print("Sorry that's not enough money. Money refunded.")

            else:

                change = round(money_offered - cost, 2)

                if change > 0:
                    print(f"Here is ${change} in change.")

                coffee_order(order_name)


coffee_machine()
