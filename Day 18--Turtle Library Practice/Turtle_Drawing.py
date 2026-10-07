from turtle import Turtle
import random
from turtle import Screen
timmy = Turtle()


timmy.shape("classic")


colours = ["red", "blue", "green", "brown",
           "purple", "pink", "yellow", "black"]


def draw_shape(sides):
    angle = 360/sides
    for i in range(sides):
        timmy.forward(70)
        timmy.right(angle)


for _ in range(3, 10):

    timmy.color(random.choice(colours))
    draw_shape(_)

screen = Screen()
screen.exitonclick()
