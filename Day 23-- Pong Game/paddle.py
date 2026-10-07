from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.goto(position)

    def move_forwards(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(), new_y)

    def move_backwards(self):
        new_y = self.ycor()-20
        self.goto(self.xcor(), new_y)
