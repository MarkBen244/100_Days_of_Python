print("Welcome to Marks Treasure Island\nYour mission as an adventurer is to safely find the treasure")
print(" \nYour teleported to another world and you find yourself at a crossroads")

choice_one = input("Are you going left or right\n")
if choice_one == "left" or choice_one == "Left":
    print("You made the right choice and you find yourself in front to a river")
    choice_two = input("Are you going to swim in the river or wait\n")
    if choice_two == "wait" or choice_two == "Wait":
        print("Congratulations you made the right choice\nYou look around and find 3 hidden doors")
        choice_three = input(
            "Which door arr you going to enter? Red, Blue or Yellow\n")
        if choice_three == "Red" or choice_three == "red":
            print("You got burnt by fire\nGame Over")
        elif choice_three == "Blue" or choice_three == "blue":
            print("You got hit by a stray blast from the Demon Lord\nGame over")
        elif choice_three == "Yellow" or choice_three == "yellow":
            print("Congratulations!!!!\n \nYou found the treasure")
        else:
            print("Game over")
    else:
        print("Game over\nCrocrodiles attacked you as you were swimming")
else:
    print("Game over\nYou fell into a hole")
