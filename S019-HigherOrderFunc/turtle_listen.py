from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


screen.listen()
# Do not use parenthesis when we are using func as argument such as move_forward vs move_forward()
# () -> triggers a function to happen there and then
# We need need to trigger func only when key is pressed
# Function as an input -> Higher order function (May not be available in other programming languages)
screen.onkey(key="space", fun=move_forwards)
# Tip: Use keyword arguments when using a method you haven't created yourself
# Keyword Arguments: screen.onkey(key="space", fun=move_forwards)
# Positional Arguments: screen.onkey("space", move_forwards) -> unsure if arguments in correct position
screen.exitonclick()
