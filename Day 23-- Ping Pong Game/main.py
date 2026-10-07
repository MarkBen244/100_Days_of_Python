from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


def half_way_line():
    line = Turtle()
    line.hideturtle()
    line.color("white")
    line.penup()
    line.goto(0, 300)
    line.setheading(270)

    for _ in range(15):
        line.pendown()
        line.forward(20)
        line.penup()
        line.forward(20)


half_way_line()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.move_forwards, "Up")
screen.onkey(r_paddle.move_backwards, "Down")
screen.onkey(l_paddle.move_forwards, "w")
screen.onkey(l_paddle.move_backwards, "s")


def game():
    game_is_on = True

    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # Detect collision with the top and bottom walls
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Detect collision with the right paddle
        if (
            ball.distance(r_paddle) < 50
            and ball.xcor() > 320
            and ball.x_move > 0
        ):
            ball.bounce_x()

        # Detect collision with the left paddle
        if (
            ball.distance(l_paddle) < 50
            and ball.xcor() < -320
            and ball.x_move < 0
        ):
            ball.bounce_x()

        # Detect when the right player misses
        if ball.xcor() > 380:
            ball.refresh_position()
            scoreboard.left_score()

        # Detect when the left player misses
        if ball.xcor() < -380:
            ball.refresh_position()
            scoreboard.right_score()


game()

screen.exitonclick()
