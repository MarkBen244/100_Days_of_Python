
print("Welcome to Mark's Treasure Island!")
print("Your mission as an adventurer is to safely find the treasure.")

print("\nYou're teleported to another world and find yourself at a crossroads.")

choice_one = input("Are you going left or right?\n").lower()

if choice_one == "left":
    print("You made the right choice and find yourself in front of a river.")

    choice_two = input("Are you going to swim in the river or wait?\n").lower()

    if choice_two == "wait":
        print("Congratulations! You made the right choice.")
        print("You look around and find 3 hidden doors.")

        choice_three = input(
            "Which door are you going to enter? Red, Blue or Yellow\n"
        ).lower()

        if choice_three == "red":
            print("You got burnt by fire.\nGame Over!")

        elif choice_three == "blue":
            print("You got hit by a stray blast from the Demon Lord.\nGame Over!")

        elif choice_three == "yellow":
            print("Congratulations!!!!")
            print("\nYou found the treasure!")

        else:
            print("Invalid choice.\nGame Over!")

    else:
        print("Game Over!")
        print("Crocodiles attacked you as you were swimming.")

else:
    print("Game Over!")
    print("You fell into a hole.")
