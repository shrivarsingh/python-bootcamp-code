import turtle as t

tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########
import random as r


def change_colour():
    R = r.random()
    G = r.random()
    B = r.random()
    tim.color(R, G, B)


tim.pensize(5)
for shape in range(3, 11):
    change_colour()
    angle = 360 / shape
    for sides in range(shape):
        tim.forward(100)
        tim.right(angle)
