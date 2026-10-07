from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def move_forwards(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + 20)

    def move_backwards(self):
        if self.ycor() > -250:
            self.goto(self.xcor(), self.ycor() - 20)
