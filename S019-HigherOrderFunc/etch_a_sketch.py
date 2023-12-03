# Etch-A-Sketch
# W -> forwards
# S -> backwards
# A -> Counter-Clockwise
# D -> Clockwise
# C -> Reset

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def rotate_counter_clockwise():
    tim.left(10)


def rotate_clockwise():
    tim.right(10)


def reset_etch_a_sketch():
    # tim.reset()
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=rotate_counter_clockwise)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="c", fun=reset_etch_a_sketch)
screen.exitonclick()
