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
    "Coffe": 1000,
    "Money": 0
}
quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01


def coffee_order():
    order_name = input("Please Confirm you order(espresso/latte/cappuccino)")
    expresso_water = MENU["espresso"]["ingredients"]["water"]
    expresso_milk = MENU["espresso"]["ingredients"]["milk"]
    expresso_coffee = MENU["espresso"]["ingredients"]["coffee"]
    expresso_cost = MENU["espresso"]["cost"]

    latte_water = MENU["latte"]["ingredients"]["water"]
    latte_milk = MENU["latte"]["ingredients"]["milk"]
    latte_coffee = MENU["latte"]["ingredients"]["coffee"]
    latte_cost = MENU["latte"]["cost"]

    cappuccino_water = MENU["cappuccino"]["ingredients"]["water"]
    cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]
    cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
    cappuccino_cost = MENU["cappuccino"]["cost"]

    # TODO 1) TAKE THEIR ORDER

    if order_name == "es":
        RESOURCES["Water"] -= expresso_water
        RESOURCES["Milk"] -= expresso_milk
        RESOURCES["Coffe"] -= expresso_coffee
        RESOURCES["Money"] += expresso_cost

    if order_name == "la":
        RESOURCES["Water"] -= latte_water
        RESOURCES["Milk"] -= latte_milk
        RESOURCES["Coffe"] -= latte_coffee
        RESOURCES["Money"] += latte_cost

    if order_name == "ca":
        RESOURCES["Water"] -= cappuccino_coffee
        RESOURCES["Milk"] -= cappuccino_milk
        RESOURCES["Coffe"] -= cappuccino_coffee
        RESOURCES["Money"] += cappuccino_cost

    if RESOURCES["Water"] < expresso_water or RESOURCES["Milk"] > expresso_milk or RESOURCES["Coffe"] > expresso_coffee:
        ternimate = print(
            "Sorry we do not have the resourses to complete your order")


def coffee_machine():
    power_on = True
    while power_on == True:
        order_name = input("What would you like? (espresso/latte/cappuccino)")

        money_offered = 0
        quarters = 0.25
        dimes = 0.10
        nickles = 0.05
        pennies = 0.01

        quarters_offered = int(input("How many quarters  "))
        dimes_offered = int(input("How many dimes "))
        nickles_offered = int(input("How many dimes "))
        pennies_offered = int(input("How many pennies "))

        for i in range(0, quarters_offered):
            money_offered += quarters
        for i in range(0, dimes_offered):
            money_offered += dimes
        for i in range(0, nickles_offered):
            money_offered += nickles
        for i in range(0, pennies_offered):
            money_offered += pennies

        if order_name == "es":
            if money_offered == 1.5:
                coffee_order()
            elif money_offered > 1.5:
                change = round(money_offered-1.5, 2)

                print(f"Here is {change} in dollars")
                coffee_order()
            else:
                return "Sorry that's not enough money. Money refunded."

        if order_name == "la":
            if money_offered == 2.5:
                coffee_order()
            elif money_offered > 2.5:
                change = round(money_offered-2.5, 2)
                print(f"Here is {change} in dollars")
                coffee_order()
            else:
                return "Sorry that's not enough money. Money refunded."

        if order_name == "ca":
            if money_offered == 3.0:
                coffee_order()
            elif money_offered > 3.0:
                change = round(money_offered-3.5, 2)
                print(f"Here is {change} in dollars")
                coffee_order()
            else:
                return "Sorry that's not enough money. Money refunded."

        if order_name == "done":
            print("Thank you for shopping with us!")
            power_on = False

        if order_name == "report":
            print(RESOURCES)

        if order_name == "off":
            power_on = False


coffee_machine()
