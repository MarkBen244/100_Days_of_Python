import random

opening_message = "Welcome to Blackjack!"
print(opening_message)


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """Calculate the score of a hand."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    """Compare the user's score with the computer's score."""
    if user_score == computer_score:
        return "******** It's a Draw *********"
    elif computer_score == 0:
        return "******** You lose *********\nYour opponent has Blackjack."
    elif user_score == 0:
        return "******** You Win *********\nYou have Blackjack!"
    elif user_score > 21:
        return "You lose, you went over 21."
    elif computer_score > 21:
        return "You win, your opponent went over 21."
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose."


def play_game():
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(
            f"\nYour cards: {user_cards}"
            f"\nYour score: {user_score}"
            f"\nComputer's first card: [{computer_cards[0]}, _]"
        )

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            should_continue = input(
                "Type 'y' to get another card or 'n' to pass: "
            ).lower()

            if should_continue == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print("\n" * 3)
    print(f"Computer's cards: {computer_cards}")
    print(f"Computer's score: {computer_score}")
    print(compare(user_score, computer_score))


while True:
    play_again = input(
        "\nDo you want to play again? Type 'yes' or 'no': ").lower()

    if play_again == "yes":
        print("\n" * 5)
        play_game()
    elif play_again == "no":
        print("Thanks for playing Blackjack! Goodbye!")
        break
    else:
        print("Please type 'yes' or 'no'.")
