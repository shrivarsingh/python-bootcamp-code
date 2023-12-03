import turtle as t

tim = t.Turtle()

########### Challenge 2 - Draw a Dashed Line ########

for _ in range(100):
    tim.forward(10)
    if tim.isdown():
        tim.penup()
    else:
        tim.pendown()
