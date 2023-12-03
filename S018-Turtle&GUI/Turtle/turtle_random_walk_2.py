import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# # My solution
# def change_colour():
#     tim.pencolor(random.choice(colours))

# tim.speed(10)
# tim.pensize(5)
# for walk in range(100):
#     change_colour()
#     tim.forward(random.randint(1, 100))
#     tim.right(90 * random.randint(0, 3))

# Angela Solution
directions = [0, 90, 180, 270]

for _ in range(200):
    tim.color(random.choice(colours))
    tim.pensize(15)
    tim.speed("fastest")
    tim.forward(100)
    tim.setheading(random.choice(directions))
