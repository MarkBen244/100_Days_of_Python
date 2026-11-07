from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
# ---------------CREATE NEW FLASH CARDS-----------------------------#

to_learn = {}
current_card = {}

try:
    data = pandas.read_csv("Day 32--Flashcard App/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv(
        "Day 32--Flashcard App/data/french_words.csv")
    to_learn = original_data.to_dict("records")
else:
    to_learn = data.to_dict("records")


flip_timer = None


def next_card():
    global current_card, flip_timer

    if flip_timer:
        window.after_cancel(flip_timer)

    if len(to_learn) == 0:
        canvas.itemconfig(card_title, text="Congratulations!")
        canvas.itemconfig(card_word, text="All words learned!")
        return

    current_card = random.choice(to_learn)

    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"])
    canvas.itemconfig(card_background, image=logo_img)

    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"])
    canvas.itemconfig(card_background, image=back_logo_img)

# ----------------------SAVE DATA----------------------------------#


def correct():
    to_learn.remove(current_card)

    data = pandas.DataFrame(to_learn)
    data.to_csv("Day 32--Flashcard App/data/words_to_learn.csv", index=False)

    next_card()


# ---------------------------UI SETUP--------------------------------#
window = Tk()
window.title("Language FlashCard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

back_logo_img = PhotoImage(file="Day 32--Flashcard App/images/card_back.png")
logo_img = PhotoImage(file="Day 32--Flashcard App/images/card_front.png")
right_img = PhotoImage(file="Day 32--Flashcard App/images/right.png")
wrong_img = PhotoImage(file="Day 32--Flashcard App/images/wrong.png")


canvas = Canvas(width=800, height=536)
card_background = canvas.create_image(400, 263, image=logo_img)
canvas.grid(column=0, row=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(
    400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(
    400, 263, text="", font=("Arial", 60, "bold"))

right_button = Button(image=right_img, highlightthickness=0, command=correct)
right_button.grid(column=0, row=1)
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=1, row=1)

next_card()
window.mainloop()
