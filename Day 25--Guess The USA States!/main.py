import turtle
import pandas
from pathlib import Path


# ---------------------------- FILE PATHS ------------------------------- #

BASE_DIR = Path(__file__).resolve().parent

image = BASE_DIR / "blank_states_img.gif"
csv_file = BASE_DIR / "50_states.csv"
output_file = BASE_DIR / "states_to_learn.csv"


# ---------------------------- SCREEN SETUP ------------------------------- #

screen = turtle.Screen()
screen.title("USA States Game")
screen.addshape(str(image))
turtle.shape(str(image))

data = pandas.read_csv(csv_file)
all_states = data["state"].to_list()
guessed_states = []


# ---------------------------- GAME LOGIC ------------------------------- #

while len(guessed_states) < 50:

    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name? Type 'Exit' to quit."
    )

    # Handle Cancel or closing the input dialog
    if answer_state is None:
        break

    answer_state = answer_state.strip().title()

    # Exit the game
    if answer_state == "Exit":
        break

    # Check the answer and prevent duplicate guesses
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)

        state_turtle = turtle.Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()

        state_data = data[data["state"] == answer_state]

        state_turtle.goto(
            state_data["x"].item(),
            state_data["y"].item()
        )

        state_turtle.write(answer_state)


# ---------------------------- SAVE MISSING STATES ------------------------------- #

missing_states = [
    state for state in all_states
    if state not in guessed_states
]

if missing_states:
    new_data = pandas.DataFrame(missing_states, columns=["State"])
    new_data.to_csv(output_file, index=False)
    print(f"Missing states saved to: {output_file}")
else:
    print("Congratulations! You guessed all 50 states.")

turtle.mainloop()
