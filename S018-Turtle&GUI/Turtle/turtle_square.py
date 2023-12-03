import turtle


tur = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
tur.shape("turtle")
tur.color("blue", "green")
tur.begin_fill()
for i in range(4):
    tur.forward(100)
    tur.right(90)
tur.end_fill()


screen.exitonclick()
