# This is another project I had done as i wa learming about conditional statements
# This shows the bill of your pizza depending on the size and toppings you want

print("Welcome to Mark Pizza Continentals\nMake your oder below:")
bill = 0
size = input("What size of pizza do you want? S, M or L:\n")
pep_s = input("Would you like peperonni with your pizza? y for Yes n for no")
ex_cheese = input("Would you like extra ex_cheese?  y for Yes n for no")
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if size == "S":
    if pep_s == "y":
        bill += 2
    else:
        bill += 3

if ex_cheese == "y":
    bill += 1
else:
    bill == bill

print(f"Your total bill is: ${bill}")
