import random
print("Welcome to Marks Nunber guessing game\n")
print("I'm thinking of a number between 1 and 100")

number = random.randint(1, 100)
difficulty = input("Do you want hard or easy mode:  ")


easy_mode = 9
hard_mode = 4


if difficulty == "easy":
    while easy_mode >= 0:
        user_guess = int(input("Guess a number : "))
        if user_guess < number:
            print("The number is higher")
            print(f"You have {easy_mode} trys left\n")
        elif user_guess > number:
            print("The number is lower")
            print(f"You have {easy_mode} trys left\n")
        else:
            print(f"You guessed the right number {number}")
        if easy_mode == 0:
            print(f"You have run out of tries\nthe number is : {number}")
        easy_mode -= 1

if difficulty == "hard":
    while hard_mode >= 0:
        user_guess2 = int(input("Guess a number:  "))
        if user_guess2 < number:
            print("The number is higher")
            print(f"You have {hard_mode} trys left\n")
        elif user_guess2 > number:
            print("The number is lower\n")
            print(f"You have {hard_mode} trys left\n")
        else:
            print(f"You guessed the right number {number}")
        if hard_mode == 0:
            print(f"You have run out of tries\nthe number is : {number}")
        hard_mode -= 1
