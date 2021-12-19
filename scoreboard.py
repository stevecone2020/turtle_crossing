from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 1

    def show_score(self):
        self.goto(-250, 260)
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def level_up(self):
        self.clear()
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)


