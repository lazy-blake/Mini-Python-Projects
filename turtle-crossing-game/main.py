from turtle import Screen
from player import Player
from car_manager import CarManager
from calculate_level import LevelCalculator
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()  # creating the player turtle
car = CarManager()  # creating the car manager
scoreboard = LevelCalculator()  # creating the scoreboard

move_speed = 0.07  # initial speed of the cars

# setting keymaps to move the player
screen.listen()
screen.onkey(player.move_up, "w")

cont = True
while cont:
    screen.update()
    time.sleep(move_speed)  # adding a delay for smoother movement

    # this statement prevents the spawn of too many cars, and creates a new car every 6 iterations
    if random.randint(1, 6) == 1:
        car.create_car()  # creating new cars

    car.move()  # moving the cars

    # this checks if the player has reached the finish line or not
    if player.ycor() > 280:
        player.new_level()
        scoreboard.increase_level()  # increasing the level
        move_speed *= 0.85

    # detecting collision with cars
    for i in car.all_cars:
        if player.distance(i) < 20 and player.xcor() < i.xcor() + 20:
            cont = False  # if the player collides with a car, the game ends
            scoreboard.game_over()  # displaying game over message

screen.exitonclick()
