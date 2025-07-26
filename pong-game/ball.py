from turtle import Turtle


class Ball(Turtle):
    def __init__(self, color):
        super().__init__()
        self.color(color)
        self.create_ball()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def create_ball(self):
        """This method is used to create the ball."""
        self.shape("circle")
        self.penup()

    def move(self):
        """This method is used to move the ball."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """This method is used to bounce the ball off the top wall."""
        self.y_move *= -1  # Reverse the y direction

    def bounce_x(self):
        self.x_move *= -1  # Reverse the x direction
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0, 0)  # Reset the ball position
        self.bounce_x()
        self.move_speed = 0.1
