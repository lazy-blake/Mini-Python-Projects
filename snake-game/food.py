from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self, color, shape):
        super().__init__()
        self.color(color)
        self.shape(shape)
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """This method is used to move the food to a new random location."""
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
