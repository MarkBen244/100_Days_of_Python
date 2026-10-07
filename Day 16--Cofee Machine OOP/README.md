# ☕ OOP Coffee Machine

A Python coffee machine simulation built using Object-Oriented Programming (OOP).

The project separates the coffee machine, menu, drinks, and payment system into different classes and modules that work together to operate the machine.

## About the Project

This project was created while learning the fundamentals of Object-Oriented Programming in Python.

Instead of keeping the entire program in one file, the application is divided into separate classes with their own responsibilities:

- `CoffeeMaker` manages ingredients and prepares drinks.
- `Menu` manages the available drinks.
- `MenuItem` represents individual drinks and their ingredients.
- `MoneyMachine` handles coins, payments, change, and profit.
- `main.py` connects the different components and runs the coffee machine.

## Features

- Order espresso, latte, or cappuccino
- Check available resources
- Process coin payments
- Calculate change
- Track machine profit
- Display resource reports
- Display available menu items
- Shut down the machine
- Handle insufficient ingredients
- Handle insufficient payment

## Project Structure

```text
coffee-machine/
├── main.py
├── coffee_maker.py
├── menu.py
└── money_machine.py
````

### `main.py`

Runs the coffee machine and connects the different classes together.

### `coffee_maker.py`

Contains the `CoffeeMaker` class, which manages ingredients and prepares drinks.

### `menu.py`

Contains:

* `Menu` — manages available drinks.
* `MenuItem` — represents individual drinks.

### `money_machine.py`

Contains the `MoneyMachine` class, which handles payments, change, and profit.

## How It Works

The program creates three main objects:

```python
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
```

The user can then select a drink.

The program:

1. Finds the requested drink.
2. Checks whether enough ingredients are available.
3. Processes the user's payment.
4. Calculates and returns change.
5. Deducts the ingredients.
6. Adds the payment to the machine's profit.
7. Serves the drink.

## Commands

| Command      | Description                          |
| ------------ | ------------------------------------ |
| `espresso`   | Order an espresso                    |
| `latte`      | Order a latte                        |
| `cappuccino` | Order a cappuccino                   |
| `report`     | Display machine resources and profit |
| `off`        | Turn off the machine                 |

## How to Run

Make sure Python is installed.

Run:

```bash
python main.py
```

No external Python packages are required.

## What I Learned

This project helped me practice:

* Classes
* Objects
* Constructors
* `__init__()`
* Instance attributes
* Methods
* Multiple Python modules
* Importing classes from other files
* Objects interacting with each other
* Encapsulation of related functionality
* Dictionaries
* Loops and conditional statements

## Future Improvements

* Improve input validation
* Add more drinks
* Add automated tests
* Improve the user interface
* Add more detailed error handling

## Author

**Mark Bernard**
