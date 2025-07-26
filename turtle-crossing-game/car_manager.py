from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LANES = [-240, -190, -140, -90, -40, 0, 40, 90, 140, 190, 240]
HORIZONTAL = [300, 305, 310, 315, 320, 325, 330, 335, 340]


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.create_car()

    # creating random cars for each lanes in random positions and appending them to the all_cars list
    def create_car(self):
        for i in LANES:
            if random.randint(1, 6) == 1:
                new_car = Turtle()
                new_car.shape("square")
                new_car.shapesize(stretch_wid=0.8, stretch_len=2.5)
                new_car.penup()
                new_car.color(random.choice(COLORS))
                new_car.setheading(180)
                new_car.goto(random.choice(HORIZONTAL), i)
                self.all_cars.append(new_car)

    # loopting through all the cars list and moving every car forward by a certain distance
    def move(self):
        for i in self.all_cars:
            if i.xcor() < -320:
                i.hideturtle()
                self.all_cars.remove(i)
            else:
                i.forward(STARTING_MOVE_DISTANCE)
