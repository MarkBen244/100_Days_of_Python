import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager, DIFFICULTIES
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")

screen.tracer(0)

difficulty_input = screen.textinput(
    "Choose Difficulty",
    "Type Easy, Normal, or Hard (default: Normal)"
)

difficulty = (difficulty_input or "normal").strip().lower()

if difficulty not in DIFFICULTIES:
    difficulty = "normal"

player = Player()
car_manager = CarManager(difficulty)
scoreboard = Scoreboard(difficulty)

screen.listen()
screen.onkey(player.move_forward, "Up")

game_is_on = True
level_message_visible = False

while game_is_on:
    time.sleep(0.1)
    screen.update()

    if level_message_visible:
        scoreboard.clear_level_message()
        level_message_visible = False

    car_manager.create_car()
    car_manager.move_cars()

    # Check for collisions between cars and player
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
            screen.update()
            break

    # Check whether the player reached the finish line
    if game_is_on and player.ycor() >= FINISH_LINE_Y:
        player.finish_line()
        car_manager.level_up()
        scoreboard.increase_level()
        scoreboard.show_level_up()
        level_message_visible = True

screen.exitonclick()
