from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 195)
        self.l_score = 0
        self.r_score = 0
        self.create_scoreboard()

    def create_scoreboard(self):
        """This method is used to create the scoreboard."""
        self.write(
            f"{self.l_score}  {self.r_score}",
            align="center",
            font=("Courier", 80, "normal"),
        )

    def update_scoreboard_left(self):
        self.l_score += 1  # Increment the left score
        self.clear()  # Clear the previous score
        self.write(
            f"{self.l_score}  {self.r_score}",
            align="center",
            font=("Courier", 80, "normal"),
        )

    def update_scoreboard_right(self):
        self.r_score += 1  # Increment the right score
        self.clear()  # Clear the previous score
        self.write(
            f"{self.l_score}  {self.r_score}",
            align="center",
            font=("Courier", 80, "normal"),
        )
