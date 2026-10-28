import math
from pathlib import Path
import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None
timer_running = False

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps, timer, timer_running

    # Cancel the active countdown, if there is one
    if timer is not None:
        window.after_cancel(timer)
        timer = None

    # Reset the timer and session counter
    reps = 0
    timer_running = False

    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer", fg=GREEN)
    checkmark.config(text="")

    # Allow the user to start again
    start_button.config(state="normal")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps, timer_running

    # Prevent multiple countdowns from running at once
    if timer_running:
        return

    timer_running = True
    start_button.config(state="disabled")

    reps += 1

    # Choose the correct session duration
    if reps % 8 == 0:
        duration = LONG_BREAK_MIN * 60
        title.config(text="Long Break", fg=RED)

    elif reps % 2 == 0:
        duration = SHORT_BREAK_MIN * 60
        title.config(text="Short Break", fg=PINK)

    else:
        duration = WORK_MIN * 60
        title.config(text="Work", fg=GREEN)

    count_down(duration)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global timer, timer_running

    # Display minutes and seconds with leading zeros
    minutes, seconds = divmod(count, 60)
    canvas.itemconfig(
        timer_text,
        text=f"{minutes:02d}:{seconds:02d}"
    )

    if count > 0:
        timer = window.after(1000, count_down, count - 1)

    else:
        # The countdown has finished
        timer = None
        timer_running = False
        start_button.config(state="normal")

        # Add a checkmark only after completing a work session
        if reps % 2 == 1:
            completed_sessions = (reps + 1) // 2
            checkmark.config(text="✔ " * completed_sessions)


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas and tomato image
canvas = tk.Canvas(
    width=200,
    height=224,
    bg=YELLOW,
    highlightthickness=0
)

# Load the image from the same folder as this Python file
image_path = Path(__file__).with_name("tomato.png")
tomato_img = tk.PhotoImage(file=str(image_path))

canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(
    100,
    130,
    text="00:00",
    fill="white",
    font=(FONT_NAME, 35, "bold")
)

canvas.grid(column=1, row=1)

# Title
title = tk.Label(
    text="Timer",
    font=(FONT_NAME, 35, "bold"),
    fg=GREEN,
    bg=YELLOW
)
title.grid(column=1, row=0)

# Start button
start_button = tk.Button(
    text="Start",
    highlightthickness=0,
    command=start_timer
)
start_button.grid(column=0, row=2)

# Reset button
reset_button = tk.Button(
    text="Reset",
    highlightthickness=0,
    command=reset_timer
)
reset_button.grid(column=2, row=2)

# Completed work sessions
checkmark = tk.Label(
    font=("Arial", 20),
    bg=YELLOW,
    fg=RED
)
checkmark.grid(column=1, row=3)

window.mainloop()
