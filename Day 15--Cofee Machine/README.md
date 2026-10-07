# ☕ Coffee Machine

A Python-based coffee machine simulation that allows users to order drinks, insert virtual coins, receive change, and manage the machine's available resources.

## About the Project

This project simulates the basic functionality of a coffee vending machine.

The machine offers three drinks:

- ☕ Espresso — $1.50
- 🥛 Latte — $2.50
- ☕ Cappuccino — $3.00

The program keeps track of the machine's water, milk, coffee, and money. Before preparing a drink, it checks whether enough ingredients are available.

## Features

- Order espresso, latte, or cappuccino
- Check available ingredients and resources
- Accept quarters, dimes, nickels, and pennies
- Calculate the amount of money inserted
- Calculate and return change
- Track money collected by the machine
- Display a resource report
- Shut down the machine using the `off` command
- Prevent orders when ingredients are insufficient
- Refund payments when insufficient money is provided

## How It Works

1. The user selects a drink.
2. The machine checks whether it has enough ingredients.
3. The user inserts coins.
4. The machine calculates the total amount inserted.
5. If there is not enough money, the payment is refunded.
6. If the payment is sufficient, the machine prepares the drink.
7. Any remaining amount is returned as change.
8. The machine updates its resources.

### Machine Commands

| Command | Description |
|---------|-------------|
| `espresso` | Order an espresso |
| `latte` | Order a latte |
| `cappuccino` | Order a cappuccino |
| `report` | Display the machine's resources |
| `off` | Shut down the machine |

## Example

```text
What would you like? (espresso/latte/cappuccino): latte

The latte costs $2.50.

How many quarters? 10
How many dimes? 0
How many nickels? 0
How many pennies? 0

Here is your latte. Enjoy!
````

## How to Run

Make sure Python is installed, then run:

```bash
python main.py
```

No external libraries are required.

## What I Learned

This project helped me practice:

* Nested dictionaries
* Functions and parameters
* `while` loops
* `if`, `elif`, and `else`
* User input
* Arithmetic operations
* Returning values from functions
* Managing program state
* Working with resources
* Basic error handling
* Formatting numbers and currency

## Future Improvements

Possible improvements for a future version:

* Add more coffee options
* Add a graphical user interface
* Improve input validation
* Add a proper coin validation system
* Add automated tests
* Separate the coffee machine logic into multiple files

## Author

**Mark Bernard**

