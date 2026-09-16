import random

opening_meassage = "Welcome to Black jack"
print(opening_meassage)


def deal_cards():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    added_cards = sum(cards)
    return added_cards


def compare(u_score, c_score):
    if u_score == c_score:
        return "********Its a Draw*********"
    elif c_score == 0:
        return "********You lose*********\n       Your opponent has a blackjack        "
    elif u_score == 0:
        return "********You Win*********\n       You have a blackjack"
    elif u_score > 21:
        return "You lose, you went over 21"
    elif c_score > 21:
        return "You win, your opponent went over 21"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"


def play_game():
    users_deck = []
    computers_deck = []
    is_game_ended = False
    comp_total = -1
    user_total = -1

    for _ in range(2):
        users_deck.append(deal_cards())
        computers_deck.append(deal_cards())

    while not is_game_ended:
        user_total = calculate_score(users_deck)
        comp_total = calculate_score(computers_deck)

        print(
            f"This are your cards :      {users_deck}\n"
            f"Your score is :      {user_total}\n"
            f"Computers first card is:    [{computers_deck[0]}, _]"
        )

        if user_total == 0 or comp_total == 0 or user_total > 21:
            is_game_ended = True
        else:
            should_continue = input(
                "Type 'y' to get another card or 'n' to pass")

            if should_continue == "y":
                users_deck.append(deal_cards())
            else:
                is_game_ended = True

    while comp_total != 0 and comp_total < 17:
        computers_deck.append(deal_cards())
        comp_total = calculate_score(computers_deck)

    print("\n"*5)
    print(f"{computers_deck}, computers score is {comp_total}")
    print(compare(user_total, comp_total))


while input("Do you want to play agian YES OR NO"):
    print("\n"*15)
    play_game()
