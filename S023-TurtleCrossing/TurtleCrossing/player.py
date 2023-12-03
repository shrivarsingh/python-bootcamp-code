from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.starting_pos()

    def move_up(self):
        self.forward(20)
    
    def check_player_won(self):
        return self.ycor() >= FINISH_LINE_Y
    
    def starting_pos(self):
        self.goto(STARTING_POSITION)
