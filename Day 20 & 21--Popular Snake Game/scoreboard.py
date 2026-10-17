
from turtle import Turtle
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data.txt"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.load_high_score()

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()

        self.update_scoreboard()

    def load_high_score(self):
        try:
            return int(DATA_FILE.read_text().strip() or "0")
        except (FileNotFoundError, ValueError):
            DATA_FILE.write_text("0")
            return 0

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score}  High Score: {self.highscore}",
            align="center",
            font=("Arial", 24, "normal")
        )

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            DATA_FILE.write_text(str(self.highscore))

        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
