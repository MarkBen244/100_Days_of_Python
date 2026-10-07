# This project was done on the the 3rd Day.
# It illustrates an amusement park ticketing app. Where your age and height are considered for entry
# It shows how much you pay according to your height and if you got your picture taken.


print("Welcome to the Mark Roller Coaster")
height = int(input("Whats your height: \n"))
price = 0
if height > 120:
    print("You can ride the rollercoastter!")
    age = int(input("How old are you: \n"))
    if 45 <= age <= 55:
        price += 0
        print("Your tickets are free!!")
    elif age > 17:
        price += 12
        print("Adult tickets are", "$", price)
    elif age < 12:
        price += 5
        print("Children tickets are", "$", price)
    elif age in range(12, 18):
        price += 7
        print("Teenagers tickets are", "$", price)
    print("Taking a picture during the ride helps to create memories!")
    picture_option = input(
        "Would you like your picture taken, Type y for Yes and n for no:\n")

    if picture_option == "y" or picture_option == "Y":
        price += 3
        print("Your total price is", "$", price)
    else:
        print("Your price is", "$", price)
else:
    print("You cannot ride due to your height")
