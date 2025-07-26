from turtle import Turtle

with open(
    "C:/Users/akash/OneDrive/Documents/Python/Projects/snake-game/data.txt", "r"
) as f:
    file = f.read()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.high_score = int(file)  # Read high score from file
        self.create_score()

    def create_score(self):
        self.penup()
        self.goto(0, 275)  # Position the scoreboard at the top center of the screen
        self.pendown()
        self.write(
            f"Score = {self.score} High Score = {self.high_score}",
            align="center",
            font=("Arial", 15, "normal"),
        )

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(
            f"Score = {self.score} High Score = {self.high_score}",
            align="center",
            font=("Arial", 15, "normal"),
        )

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(
                "C:/Users/akash/OneDrive/Documents/Python/Projects/snake-game/data.txt",
                "w",
            ) as f:
                f.write(str(self.high_score))
        self.score = 0
        self.clear()
        self.penup()
        self.write(
            f"Score = {self.score} High Score = {self.high_score}",
            align="center",
            font=("Arial", 15, "normal"),
        )
