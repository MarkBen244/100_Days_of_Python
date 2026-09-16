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
print("Hi there\nWelcome to Mark's python calculator")


def calcution(number1, number2):
    """This is the first set of numbers calculation"""

    result = 0
    opertion = input(
        "Pick an operation \nAddition (+)\nSubtraction(-)\nMultiplication(*)\nDivision(/)\nWhat is your opertion:  ")
    if opertion == "+":
        result += number1+number2
        print(f"{number1} + {number2} = {result}")

    elif opertion == "-":
        result += number1-number2
        print(f"{number1} - {number2} = {result}")

    elif opertion == "*":
        result += number1*number2
        print(f"{number1} * {number2} = {result}")

    elif opertion == "/":
        result += number1/number2
        print(f"{number1} / {number2} = {result}")

    else:
        output = print("Invalid opertion")
        return output

    should_continue = input(
        f"Type \n'y' to continue calculating with {result}\n'n' to start a new calculation\n'e' to end the program\n")

    if should_continue == "y":
        print("\n"*5)
        print(f"Previous Number {result}")
        t_number = int(input("What is the next number?  "))
        calcution(result, t_number)
    elif should_continue == "n":
        print("\n"*8)
        print(art)
        print("Welcome back to Mark's python calculator")
        f1_number = int(input("What is your first number?   "))
        f2_number = int(input("What is your next number?   "))
        calcution(f1_number, f2_number)
    else:
        print(f"This was the final result: {result}")
        final_message = print(
            "Thank you for using the Mark's Calculator, Bye!")
        return final_message


f_number = int(input("What is your first number?   "))
s_number = int(input("What is the next number?  "))

calcution(f_number, s_number)
