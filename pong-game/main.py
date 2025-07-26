from turtle import Screen
from paddle import Paddle  # Import the Paddle class from the paddle module
from ball import Ball  # Import the Ball class from the ball module
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)  # Disable automatic screen updates for smoother animation

paddle_r = Paddle("white", 375, 0)  # Create the left paddle
paddle_l = Paddle("white", -375, 0)  # Create the right paddle
ball = Ball("white")  # Create the ball
scoreboard = Scoreboard()  # Create the scoreboard

# to move the padddles with the keyboard
screen.listen()
screen.onkey(paddle_l.move_up, "w")
screen.onkey(paddle_l.move_down, "s")
screen.onkey(paddle_r.move_up, "Up")
screen.onkey(paddle_r.move_down, "Down")


game_is_on = True  # Variable to control the game loop
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)  # Control the speed of the game loop
    ball.move()  # Move the ball

    # bounce the ball from the top and the bottom walls
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()  # Bounce the ball off the top and bottom walls

    # bounce the ball of the left and the right paddles
    elif (
        ball.distance(paddle_r) < 40
        and ball.xcor() > 340
        or ball.distance(paddle_l) < 40
        and ball.xcor() < -340
    ):
        ball.bounce_x()  # Bounce the ball off the paddles

    # if any of the paddles misses the ball then updating score and resets the balls position
    if ball.xcor() > 395:
        scoreboard.update_scoreboard_left()  # Update the left score
        ball.reset()

    if ball.xcor() < -395:
        scoreboard.update_scoreboard_right()
        ball.reset()


screen.exitonclick()
