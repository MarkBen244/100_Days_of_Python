from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from Scoreboard import Scoreboard
import time
import random

game_is_on = True


# Half Way line
def half_way_line():

    line = Turtle()
    line.penup()
    line.goto(0, 350)
    line.color("red")
    line.shapesize(2, 1)
    line.setheading(270)
    line.pendown()
    line.forward(800)


half_way_line()


# Screen Class
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
line = Turtle()


screen.listen()
screen.onkey(key="Up", fun=r_paddle.move_forwards)
screen.onkey(key="Down", fun=r_paddle.move_backwards)
screen.onkey(key="w", fun=l_paddle.move_forwards)
screen.onkey(key="s", fun=l_paddle.move_backwards)


def game():
    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # Detect Collision with the wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Detect collision with paddle
        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()

        if ball.xcor() > 380:
            ball.refresh_position()
            scoreboard.left_score()

        if ball.xcor() < -380:
            ball.refresh_position()
            scoreboard.right_score()


game()
screen.exitonclick()
