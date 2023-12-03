from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
DATA = "data.txt"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.load_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_score()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def load_score(self):
        with open(DATA, mode="r") as data:
            self.high_score = int(data.read())

    def save_score(self):
        with open(DATA, mode="w") as data:
            data.write(str(self.high_score))
