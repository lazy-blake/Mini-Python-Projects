from turtle import Screen
import time
from snake import Snake  # Import the Sanke class from the snake module
from food import Food  # Import the Food class from the food module
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# create 3 boxes of snake
snake = Snake("white", 3)  # Create a Snake object with color "white" and 3 segments)
food = Food("blue", "circle")
scoreboard = Scoreboard()  # Create a Scoreboard object

screen.listen()
screen.onkey(snake.up, "w")  # Bind the  w to the snake's up method
screen.onkey(snake.down, "s")  # Bind the s to the snake's down method
screen.onkey(snake.left, "a")  # Bind the a key to the snake's left method
screen.onkey(snake.right, "d")  # Bind the d key to the snake's right method

screen.update()

cont = True
while cont:
    """this update the screen everytime after the all three boxes move,
    so that the snake can be seen moving and we cant see the wierd movement of the snake."""
    screen.update()
    time.sleep(0.1)  # Control the speed of the game

    snake.move()  # Move the snake
    """it checks the distance between the snake head and the food, and then 
    spawn the food in new location if the distance is less than 15 pixels."""
    if snake.snakes[0].distance(food) < 15:
        snake.create_snake(1)
        scoreboard.update_score()
        food.refresh()
        # Add a new segment to the snake

    # checking collision with the wall
    if (
        snake.snakes[0].xcor() > 280
        or snake.snakes[0].xcor() < -295
        or snake.snakes[0].ycor() > 295
        or snake.snakes[0].ycor() < -290
    ):
        scoreboard.game_over()
        snake.reset()

    # slicing the loop from the 2nd snake to the last snake, so the head doesn't collide with itself
    for i in snake.snakes[1:]:
        if snake.snakes[0].distance(i) < 10:
            scoreboard.game_over()


screen.exitonclick()
