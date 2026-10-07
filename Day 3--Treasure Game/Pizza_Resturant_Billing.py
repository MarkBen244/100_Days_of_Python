
print("Welcome to Mark Pizza Continentals")
print("Make your order below:")

bill = 0

size = input("What size of pizza do you want? S, M or L:\n").upper()
pepperoni = input(
    "Would you like pepperoni with your pizza? y for Yes, n for No:\n").lower()
extra_cheese = input(
    "Would you like extra cheese? y for Yes, n for No:\n").lower()

# Pizza size
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Invalid pizza size.")
    exit()

# Pepperoni
if pepperoni == "y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# Extra cheese
if extra_cheese == "y":
    bill += 1

print(f"Your total bill is: ${bill}")
