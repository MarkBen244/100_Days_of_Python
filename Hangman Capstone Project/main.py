import random


HANGMAN_STAGES = [
    '''
       +---+
       |   |
           |
           |
           |
           |
     =========
''',
    '''
       +---+
       |   |
       O   |
           |
           |
           |
     =========
''',
    '''
       +---+
       |   |
       O   |
       |   |
           |
           |
     =========
''',
    '''
       +---+
       |   |
       O   |
      /|   |
           |
           |
     =========
''',
    '''
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
     =========
''',
    '''
       +---+
       |   |
       O   |
      /|\\  |
       |   |
           |
     =========
''',
    '''
       +---+
       |   |
       O   |
      /|\\  |
       |   |
      /    |
           |
     =========
''',
    '''
       +---+
       |   |
       O   |
      /|\\  |
       |   |
      / \\  |
           |
     =========
''',
    '''
       +---+
       |   |
       X   |
      /|\\  |
       |   |
      / \\  |
           |
     =========
'''
]


def visual(lives):
    print(HANGMAN_STAGES[8 - lives])


word_list = [
    "aardvark",
    "baboon",
    "camel",
    "ant",
    "badger",
    "bat",
    "bear",
    "beaver",
    "cat",
    "clam",
    "cobra",
    "frog",
    "goat",
    "zebra"
]

chosen_word = random.choice(word_list)

print("The theme of this Hangman game is animals.")

display = ["_" for _ in chosen_word]
lives = 8
correct_letters = []
game_over = False

print(" ".join(display))

while not game_over:
    print(
        f"\n********************** {lives}/8 LIVES LEFT **********************")

    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You have already guessed {guess}.")
        continue

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in chosen_word:
        correct_letters.append(guess)

        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = letter

        print("Good guess!")

    else:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word.")
        print("You lose a life.")

    print("Word to guess: " + " ".join(display))
    visual(lives)

    if "_" not in display:
        print(
            "\n********************* YOU WIN! *********************"
            "\nCONGRATULATIONS!"
        )
        game_over = True

    elif lives == 0:
        print(
            f"\n********************* GAME OVER *********************"
            f"\nThe word was: {chosen_word}"
        )
        game_over = True
