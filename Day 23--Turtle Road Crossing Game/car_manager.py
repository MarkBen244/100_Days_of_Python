from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

DIFFICULTIES = {
    "easy": (3, 0.4),
    "normal": (5, 0.75),
    "hard": (7, 1.0),
}


class CarManager:
    def __init__(self, difficulty="normal"):
        self.all_cars = []

        difficulty = difficulty.lower()
        self.car_speed, self.move_increment = DIFFICULTIES.get(
            difficulty, DIFFICULTIES["normal"]
        )

    def create_car(self):
        if random.randint(1, 6) == 1:
            random_y = random.randint(-250, 250)

            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(320, random_y)
            new_car.color(random.choice(COLORS))

            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars[:]:
            car.backward(self.car_speed)

            if car.xcor() < -330:
                car.hideturtle()
                car.clear()
                self.all_cars.remove(car)

    def level_up(self):
        self.car_speed += self.move_increment
