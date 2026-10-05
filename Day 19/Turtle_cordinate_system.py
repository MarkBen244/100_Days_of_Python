from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.back(10)


def move_right():
    new = tim.heading()-10
    tim.setheading(new)


def move_left():
    new = tim.heading()+10
    tim.setheading(new)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
