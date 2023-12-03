from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(x=0, y=265)
        self.hideturtle()
        self.pencolor("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        display = f"Score: {self.score}"
        self.clear()
        self.write(arg=display, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self, point):
        self.score += point
        self.update_scoreboard()
