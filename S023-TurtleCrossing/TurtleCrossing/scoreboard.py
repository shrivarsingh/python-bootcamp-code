from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.level = 0.1
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.update_score()

    def update_text(self):
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=FONT)
    
    def update_score(self):
        self.score += 1
        self.level *= 0.9
        self.update_text()
    
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
