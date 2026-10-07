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
    },
}

RESOURCES = {
    "Water": 3000,
    "Milk": 2000,
    "Coffee": 1000,
    "Money": 0,
}


def coffee_order(order_name):
    """Check resources, make the coffee, and update the machine."""

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
    """Run the coffee machine."""

    while True:
        order_name = input(
            "What would you like? (espresso/latte/cappuccino): "
        ).lower()

        if order_name == "off":
            print("Coffee machine shutting down.")
            break

        elif order_name == "report":
            print("\nCurrent resources:")
            print(f"Water: {RESOURCES['Water']}ml")
            print(f"Milk: {RESOURCES['Milk']}ml")
            print(f"Coffee: {RESOURCES['Coffee']}g")
            print(f"Money: ${RESOURCES['Money']:.2f}")
            print()

        elif order_name not in MENU:
            print("Please choose espresso, latte or cappuccino.")

        else:
            cost = MENU[order_name]["cost"]

            print(f"The {order_name} costs ${cost:.2f}.")

            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickels = int(input("How many nickels? "))
            pennies = int(input("How many pennies? "))

            money_offered = (
                quarters * 0.25
                + dimes * 0.10
                + nickels * 0.05
                + pennies * 0.01
            )

            if money_offered < cost:
                print("Sorry, that's not enough money. Money refunded.")
                continue

            change = round(money_offered - cost, 2)

            # Check resources before accepting payment.
            if not coffee_order(order_name):
                print("Money refunded.")
                continue

            if change > 0:
                print(f"Here is ${change:.2f} in change.")


coffee_machine()
