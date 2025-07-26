from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, color, x, y):
        super().__init__()
        self.color(color)
        self.shape("square")
        self.create_paddle(x, y)

    def create_paddle(self, x, y):
        """This method is used to create the paddle at a specific position."""
        self.speed("fastest")  # Set the speed to the fastest for immediate drawing"
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, y)  # Initial position of the paddle

    def move_up(self):
        """This method is used to move the paddle up by 20 pixels."""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        """This method is used to move the paddle down by 20 pixels."""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
