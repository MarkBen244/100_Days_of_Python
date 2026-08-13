import random
word_list = ["aardvark", "baboon", "camel", "ant", "babboon", "badger",
             "bat", "bear", "beaver", "cat", "clam", "cobra", "frog", "goat", "zebra"]

# GENERATE A RANDOM WORD
chosen_word = random.choice(word_list)
print(chosen_word)
print("The theme of this hangman is animals")
# # ADDING A PLACE_HOlDER FOR EACH LETTER OF THE WORD
place_holder = ("")
for letter in chosen_word:
    place_holder = "_"+place_holder
print(place_holder)

# USERS GUESSES LETTER
lives = 6
correct_letters = []
game_over = False
while not game_over:
    print(f"************{lives}/6 LIVES LEFT***********")
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
        print("********YOU WIN********")
        game_over = True

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, thats not on the word.\nYou lose a life.")

        if lives == 0:
            game_over = True
            print(
                f"You have used up all 6 lives\nGame over\nThe word is {chosen_word}")
