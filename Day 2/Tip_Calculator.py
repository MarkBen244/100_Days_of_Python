# This is my first python Project, This program hepls friends who go out to eat
# And decides to split the bill among themselves.It also accounts for the tip to the waiter.
print("Welcome to the  My Python tip calculator")
a = float(input("What was the total bill?\n$"))
b = int(input("How much tip would you like to give? 10, 12 or 15\n%"))
c = int(input("How many people to split the bill?\n"))

x = (b/100)
y = ((a*x)+a)
z = (y/7)
m = (round(z, 2))
print(f"Every on should pay {m}")
