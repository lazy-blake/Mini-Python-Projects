from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.create_turtle()

    def create_turtle(self):
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    # to move the turtle up
    def move_up(self):
        self.forward(MOVE_DISTANCE)

    # to reset the turtle position when the player reaches the finish line
    def new_level(self):
        self.goto(STARTING_POSITION)
