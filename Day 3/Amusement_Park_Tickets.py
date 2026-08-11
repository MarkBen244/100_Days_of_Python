# a = int(input("What is your number: "))
# if a % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

print("Welcome to the Mark Roller Coaster")
height = int(input("Whats your height: \n"))
if height > 120:
    print("You can ride the rollercoastter!")
    age = int(input("How old are you: \n"))
    if 45 <= age <= 55:
        price = 0
        print("Mid life crisis tickets are free!!")
    elif age > 18:
        price = 12
        print("Adult tickets are", "$", price)
    elif age < 12:
        price = 5
        print("Children tickets are", "$", price)
    elif age in range(12, 19):
        price = 7
        print("Teenagers tickets are", "$", price)
    print("Taking a picture during the ride helps to create memories!")
    picture_option = input(
        "Would you like your picture taken, Type y for Yes and n for no:\n")

    if picture_option == "y":
        print("Your total price is", "$", price+3)
    else:
        print("Your price is", "$", price)
else:
    print("You cannot ride due to your height")
