# We all struggle with passwords.
# Ths program generates a STRONG password for you, depending on the number of letters,numbers and symbols you want.


import random
letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]


numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '*', '&']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How mant letters do you want in your password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

# Easy mode

# password = ""
# for i in range(1, nr_letters+1):
#     randon_char = random.choice(letters)
#     password += randon_char

# for i in range(1, nr_numbers+1):
#     randon_num = random.choice(numbers)
#     password += randon_num

# for i in range(1, nr_symbols+1):
#     randon_sym = random.choice(symbols)
#     password += randon_sym

# print(password)


# Hard Mode 1

# password = ""
# for i in range(1, nr_letters+1):
#     randon_char = random.choice(letters)
#     password += randon_char

# for i in range(1, nr_numbers+1):
#     randon_num = random.choice(numbers)
#     password += randon_num

# for i in range(1, nr_symbols+1):
#     randon_sym = random.choice(symbols)
#     password += randon_sym

# print(password)

# re_password = list(password)
# random.shuffle(re_password)
# shuffled = "".join(re_password)
# print("Your generated password is:\n", shuffled)

# Hard Mode 2

password_list = []
for i in range(0, nr_letters):
    password_list.append(random.choice(letters))
for i in range(0, nr_symbols):
    password_list.append(random.choice(symbols))
for i in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""
for i in password_list:
    password += i
print("Your password is:\n", password)
