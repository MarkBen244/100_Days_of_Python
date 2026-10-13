from turtle import Turtle

FONT = ("Courier", 18, "normal")
MESSAGE_FONT = ("Courier", 24, "bold")
HIGH_SCORE_FILE = "high_score.txt"


class Scoreboard(Turtle):
    def __init__(self, difficulty):
        super().__init__()

        self.level = 1
        self.high_score = self.load_high_score()
        self.difficulty = difficulty.title()

        self.hideturtle()
        self.penup()

        self.update_scoreboard()

    def load_high_score(self):
        try:
            with open(HIGH_SCORE_FILE, "r", encoding="utf-8") as file:
                return max(1, int(file.read().strip()))
        except (FileNotFoundError, ValueError):
            return 1

    def save_high_score(self):
        with open(HIGH_SCORE_FILE, "w", encoding="utf-8") as file:
            file.write(str(self.high_score))

    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 260)
        self.write(
            f"Level: {self.level}   Best: {self.high_score}",
            align="left",
            font=FONT,
        )

        self.goto(280, 260)
        self.write(
            f"Difficulty: {self.difficulty}",
            align="right",
            font=("Courier", 12, "normal"),
        )

    def increase_level(self):
        self.level += 1

        if self.level > self.high_score:
            self.high_score = self.level
            self.save_high_score()

        self.update_scoreboard()

    def show_level_up(self):
        self.goto(0, 0)
        self.write(
            "LEVEL UP!",
            align="center",
            font=MESSAGE_FONT,
        )

    def clear_level_message(self):
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(
            "GAME OVER",
            align="center",
            font=MESSAGE_FONT,
        )

        self.goto(0, -35)
        self.write(
            f"You reached Level {self.level}",
            align="center",
            font=FONT,
        )

        self.goto(0, -65)
        self.write(
            f"Best Level: {self.high_score}",
            align="center",
            font=FONT,
        )
