from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.speed("fastest")
        self.goto(position)
        self.speed("normal")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)  # All turtles start at size 20 x 20

    def go_up(self):
        new_pos= self.ycor() + 20
        self.goto(self.xcor(), new_pos)


    def go_down(self):
        new_pos= self.ycor() - 20
        self.goto(self.xcor(), new_pos)
