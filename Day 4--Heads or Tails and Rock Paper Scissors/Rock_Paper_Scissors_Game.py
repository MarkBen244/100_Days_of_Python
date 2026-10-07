
import random

print("Welcome to Mark's Rock Paper Scissors Game!")

players_pick = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ")
)

if players_pick not in [0, 1, 2]:
    print("Please pick from the available options.")
else:
    weapons = ["Rock", "Paper", "Scissors"]

    player_weapon = weapons[players_pick]
    bot = random.randint(0, 2)
    bot_weapon = weapons[bot]

    print(f"You chose: {player_weapon}")
    print(f"Robot chose: {bot_weapon}")

    if players_pick == bot:
        print("It's a draw!")

    elif (
        (players_pick == 0 and bot == 2)
        or (players_pick == 1 and bot == 0)
        or (players_pick == 2 and bot == 1)
    ):
        print("You win!")

    else:
        print("You lose!")
