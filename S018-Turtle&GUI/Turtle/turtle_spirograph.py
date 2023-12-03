import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########

tim.speed("fastest")

# # My solution
# for i in range(72):
#     tim.color(random_color())
#     tim.circle(50)
#     tim.left(5)

# # Angela Solution
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)

# draw_spirograph(5)

# My Test
def draw_spirograph_random_color(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(150)
        tim.setheading(tim.heading() + size_of_gap)

def draw_spirograph_white(size_of_gap):
    tim.color(255, 255, 255)
    for _ in range(int(360 / size_of_gap)):
        tim.circle(150)
        tim.setheading(tim.heading() + size_of_gap)

def draw_spirograph_black(size_of_gap):
    tim.color(0, 0, 0)
    for _ in range(int(360 / size_of_gap)):
        tim.circle(150)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph_random_color(3)
draw_spirograph_white(6)
draw_spirograph_black(9)

screen = t.Screen()
screen.exitonclick()
