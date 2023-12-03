from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        # Calls turtle init method inside the food init method
        self.shape("circle")  # We can use these methods as we inheriting from the superclass
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("OrangeRed")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
