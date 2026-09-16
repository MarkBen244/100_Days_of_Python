import random
opening_meassage = "Welcome to Black jack"
print(opening_meassage)
cards = [11, 11, 11, 11, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# TODO 1 DEAL THE PLAYER AND COMPUTER THEIR CARDS

users_deck = []
computers_deck = []


def calculate():
    user_total = 0
    comp_total = 0
    for num in range(0, 1):
        deal = random.choice(cards)
        users_deck.append(deal)
    for num in range(0, 1):
        deal = random.choice(cards)
        users_deck.append(deal)
    for num in range(0, 1):
        deal = random.choice(cards)
        computers_deck.append(deal)
    for num in range(0, 1):
        deal = random.choice(cards)
        computers_deck.append(deal)
    print(
        f"This are your cards {users_deck}\nThis are the computers cards{computers_deck}")

    for num in users_deck:
        user_total += num

    for num in computers_deck:
        comp_total += num
    print(f"Your total is   {user_total}\ncomputers total   {comp_total}")

    lose_statement = "*********YOU LOSE!!***************\nTry Again next time"
    if user_total == 21:
        print("***********YOU WIN!!  BLACKJACK******************")
    elif comp_total == 21:
        return lose_statement
    if comp_total == 21 and user_total == 21:
        print("Its a Draw")

    if user_total > 21:
        for num in range(len(users_deck)):
            if users_deck[num] == 11:
                users_deck[num] = 1
                print(user_total)
            else:
                return lose_statement
    elif user_total < 21:
        should_continue = input("Yes or No  ")
        if should_continue == "y":
            calculate()


calculate()
