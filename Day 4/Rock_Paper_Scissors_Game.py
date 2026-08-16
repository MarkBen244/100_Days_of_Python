# This is a Rock Paper Scissors game. the user picks an option and the robot picks a random option.
import random
print("Welcoe to the Marks Rock Paper Scissors Game")
players_pick = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))
weapon = 0
bot_weapon = 0
if players_pick == 0:
    weapon = "Rock"
    print("YOU CHOOSE: Rock")
    bot = random.randint(0, 2)
    if bot == 0:
        bot_weapon = "Rock"
    if bot == 1:
        bot_weapon = "Paper"
    if bot == 2:
        bot_weapon = "Scissors"

    print(bot_weapon)

    if bot == 1:
        print("Robot Choose Paper:\nYou lose")
    elif bot == 2:
        print("Robot Choose Scissors:\nYou win")
    else:
        print("Robot Choose Rock:\nIts a Draw")
elif players_pick == 1:
    weapon = "Paper"
    print("YOU CHOOSE: Paper")
    bot = random.randint(0, 2)
    if bot == 0:
        bot_weapon = "Rock"
    if bot == 1:
        bot_weapon = "Paper"
    if bot == 2:
        bot_weapon = "Scissors"

    print(bot_weapon)

    if bot == 1:
        print("Robot Choose Paper:\nYou draw")
    elif bot == 2:
        print("Robot Choose Scissors:\nYou lose")
    else:
        print("Robot Choose Rock:\nYou win")
elif players_pick == 2:
    weapon = "Scissors"
    print("YOU CHOOSE: Scissors")
    bot = random.randint(0, 2)
    if bot == 0:
        bot_weapon = "Rock"
    if bot == 1:
        bot_weapon = "Paper"
    if bot == 2:
        bot_weapon = "Scissors"

    if bot == 1:
        print("Robot Choose Paper:\nYou win")
    elif bot == 2:
        print("Robot Choose Scissors:\nYou draw")
    else:
        print("Robot Choose Rock:\nIts a lose")
else:
    print("Please pick from the options available")
