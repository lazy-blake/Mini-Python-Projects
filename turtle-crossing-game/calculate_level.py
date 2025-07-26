from turtle import Turtle


class LevelCalculator(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.level = 1
        self.penup()
        self.speed("fastest")
        self.create_scoreboard()

    def create_scoreboard(self):
        self.penup()
        self.hideturtle()
        self.goto(-240, 260)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 15, "bold"))

    # increase the level of the game  when they reach the finish line
    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=("Courier", 15, "bold"))

    # calling this method when the player hits a car
    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 20, "bold"))
