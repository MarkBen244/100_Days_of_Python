import random
word_list = ["aardvark", "baboon", "camel"]

# GENERATE A RANDOM WORD
chosen_word = random.choice(word_list)
print(chosen_word)

# # ADDING A PLACE_HOlDER FOR EACH LETTER OF THE WORD
place_holder = ("")
for letter in chosen_word:
    place_holder = "_ "+place_holder
print(place_holder)

# USERS GUESSES LETTER
lives = 6
correct_letters = []
while lives > 0:
    lives -= 1
    guess = str(input("Guess a letter: ")).lower()
    display = ""
    for letter in chosen_word:
        if guess == letter:
            display += letter + " "
            correct_letters.append(guess)

        elif letter in correct_letters:
            display += letter

        else:
            display += "_ "
    print(display)

    if "_" not in display:
        print("You win")

if lives == 0:
    print("You have used up all 6 lives\nGame over")
