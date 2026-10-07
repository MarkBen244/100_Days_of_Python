import turtle as t
import random
from turtle import Screen
timmy = t.Turtle()
t.colormode(225)


timmy.shape("classic")


def random_colour():
    r = random.randint(0, 225)
    g = random.randint(0, 225)
    b = random.randint(0, 225)
    colur = (r, b, g)
    return colur


direction = [0, 90, 180, 270]

timmy.speed("fastest")


def spriral(size):

    for _ in range(int(360/size)):

        timmy.circle(100)
        timmy.setheading(timmy.heading()+size)


spriral(5)

screen = Screen()
screen.exitonclick()
