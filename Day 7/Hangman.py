import random


def visual(lives):
    if lives == 8:
        print('''
               +---+
               |   |
                   |
                   |
                   |
                   |
             =========''')
    elif lives == 7:
        print('''
               +---+
               |   |
               O   |
                   |
                   |
                   |
                   |
             =========''')
    elif lives == 6:
        print('''
               +---+
               |   |
               O   |
               |   |
                   |
                   |
                   |
             =========''')
    elif lives == 5:
        print('''
               +---+
               |   |
               O   |
              /|   |
                   |
                   |
                   |
             =========''')
    elif lives == 4:
        print('''
               +---+
               |   |
               O   |
              /|\\  |
                   |
                   |
                   |
             =========''')
    elif lives == 3:
        print('''
               +---+
               |   |
               O   |
              /|\\  |
               |   |
                   |
                   |
             =========''')
    elif lives == 2:
        print('''
               +---+
               |   |
               O   |
              /|\\  |
               |   |
              /    |
                   |
             =========''')
    elif lives == 1:
        print('''
               +---+
               |   |
               O   |
              /|\\  |
               |   |
              / \\  |
                   |
             =========''')
    elif lives == 0:
        print('''
               +---+
               |   |
               X   |
              /|\\  |
               |   |
              / \\  |
                   |
             =========''')


word_list = ["aardvark", "baboon", "camel", "ant", "babboon", "badger",
             "bat", "bear", "beaver", "cat", "clam", "cobra", "frog", "goat", "zebra"]

# GENERATE A RANDOM WORD
chosen_word = random.choice(word_list)
print("The theme of this hangman is animals")
# # ADDING A PLACE_HOlDER FOR EACH LETTER OF THE WORD
place_holder = ("")
for letter in chosen_word:
    place_holder = "_"+place_holder
print(place_holder)

# USERS GUESSES LETTER
lives = 8

correct_letters = []
game_over = False
while not game_over:
    print(f"**********************{lives}/8 LIVES LEFT*********************")
    guess = str(input("Guess a letter: ")).lower()
    if guess in correct_letters:
        print(f"You have already guessed {guess}")
    display = ""
    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_letters.append(guess)

        elif letter in correct_letters:
            display += letter

        else:
            display += "_ "

    print("Word to guess     " + display)

    if "_" not in display:
        print(
            "*********************YOU WIN*****************************\nCONGRATULATIONS!!!")
        game_over = True

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, thats not on the word.\nYou lose a life.")

        if lives == 0:
            game_over = True
            print(
                f"You have used up all 6 lives\nGame over\nThe word is {chosen_word}")
    visual(lives)
