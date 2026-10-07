art = """
 __________
| ________ |
||12345678||
|"""    """|
|[M|#|C][-]|
|[7|8|9][+]|
|[4|5|6][x]|
|[1|2|3][%]|
|[.|O|:][=]|
"----------"
"""

print(art)
print("Hi there!")
print("Welcome to Mark's Python Calculator")


def calculation(number1, number2):
    """Perform a calculation using two numbers."""

    operation = input(
        "\nPick an operation:\n"
        "Addition (+)\n"
        "Subtraction (-)\n"
        "Multiplication (*)\n"
        "Division (/)\n"
        "What is your operation: "
    )

    if operation == "+":
        result = number1 + number2
        print(f"{number1} + {number2} = {result}")

    elif operation == "-":
        result = number1 - number2
        print(f"{number1} - {number2} = {result}")

    elif operation == "*":
        result = number1 * number2
        print(f"{number1} * {number2} = {result}")

    elif operation == "/":
        if number2 == 0:
            print("You cannot divide by zero.")
            return

        result = number1 / number2
        print(f"{number1} / {number2} = {result}")

    else:
        print("Invalid operation.")
        return

    should_continue = input(
        f"\nType 'y' to continue calculating with {result}\n"
        "'n' to start a new calculation\n"
        "'e' to end the program\n"
    ).lower()

    if should_continue == "y":
        print("\n" * 3)
        print(f"Previous number: {result}")

        next_number = int(input("What is the next number? "))
        calculation(result, next_number)

    elif should_continue == "n":
        print("\n" * 3)
        print(art)
        print("Welcome back to Mark's Python Calculator")

        first_number = int(input("What is your first number? "))
        second_number = int(input("What is your next number? "))

        calculation(first_number, second_number)

    elif should_continue == "e":
        print(f"\nThis was the final result: {result}")
        print("Thank you for using Mark's Calculator. Bye!")

    else:
        print("Invalid choice. Calculator ended.")


first_number = int(input("What is your first number? "))
second_number = int(input("What is the next number? "))

calculation(first_number, second_number)
