from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self, color, how_many_snakes):
        self.snakes = []  # Initialize the list of snakes
        self.color = color
        self.create_snake(how_many_snakes)

    def create_snake(self, how_many_snakes):
        for i in range(how_many_snakes):
            """this loop runs (how_many_snakes) times and create 3 boxes for the snake 
            and move them so that thay look like one snake"""

            snake = Turtle("square")
            snake.penup()
            snake.color(self.color)

            # to resolve the flashing of the snake when it is created after eating a food
            if self.snakes:
                tail = self.snakes[-1]
                snake.goto(tail.xcor(), tail.ycor())
            else:
                # Initial creation: stagger the segments
                if i > 0:
                    snake.goto(-20 * i, 0)

            self.snakes.append(snake)

    def move(self):
        """this loop goes from the last snake in the list to the first snake in the list ,
        thats why the step count is (-1) to reduce 1 everytime the loops runs. Then when the loop runs
        the x and y stores the coordinates of the previous snakes position, so that the current snake
        can move to that location. This creates the effect of the snake moving as a whole."""

        for i in range(len(self.snakes) - 1, 0, -1):  # start=2,stop=0,step=-1
            x = self.snakes[i - 1].xcor()
            y = self.snakes[i - 1].ycor()
            self.snakes[i].goto(x, y)

        self.snakes[0].forward(20)

    def up(self):
        if self.snakes[0].heading() != DOWN:
            self.snakes[0].setheading(UP)  # Set the direction to up

    def down(self):
        if self.snakes[0].heading() != UP:
            self.snakes[0].setheading(DOWN)  # Set the direction to down

    def left(self):
        if self.snakes[0].heading() != RIGHT:
            self.snakes[0].setheading(LEFT)  # Set the direction to left

    def right(self):
        if self.snakes[0].heading() != LEFT:
            self.snakes[0].setheading(RIGHT)  # Set the direction to right

    def reset(self):
        """This method reset the snake position in the center of the screen
        and clears the previous snake segments , when the snake collides with the wall or itself."""
        for i in self.snakes:
            i.goto(1000, 1000)  # Move each snake segment off-screen
        self.snakes.clear()  # Clear the list of snakes
        self.create_snake(3)  # Recreate the snake with 3 segments
        self.snakes[0].goto(0, 0)  # Reset the position to the center of the screen
