from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.move_speed = STARTING_MOVE_DISTANCE
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color("black", random.choice(COLORS))
        self.goto(300, random.randint(-250, 250))
    
    def move_car_across(self):
        new_x_pos = self.xcor() - self.move_speed
        self.goto(new_x_pos, self.ycor())
    
    def update_speed(self):
        self.move_speed += MOVE_INCREMENT
