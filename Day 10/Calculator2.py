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


def add(n1, n2):
    return n1+n2


def subtract(n1, n2):
    return n1-n2


def multiply(n1, n2):
    return n1*n2


def divide(n1, n2):
    return n1/n2


opertions = {"+": add,
             "-": subtract,
             "*": multiply,
             "/": divide,
             }


def calculator():
    print(art)
    should_accumulate = True
    num1 = float(input("What is your first number?   "))

    while should_accumulate == True:
        for symbols in opertions:
            print(symbols)
        opertion_symbol = input("Pick an operation ")
        num2 = float(input("What is your next number?   "))
        answer = opertions[opertion_symbol](num1, num2)
        print(
            f"{num1} {opertion_symbol} {num2} = {answer}")

        choice = input(
            f"Type \n'y' to continue calculating with {answer}\n'n' to start a new calculation.")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n"*10)
            calculator()


calculator()
