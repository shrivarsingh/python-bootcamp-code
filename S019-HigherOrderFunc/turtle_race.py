import turtle
import random

is_race_on = False
screen = turtle.Screen()
screen.bgcolor("gray50")
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
print(f"You betted for {user_bet.title()} to win.")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-125, -75, -25, 25, 75, 125]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color("black", colors[turtle_index])
    new_turtle.penup()
    random_y_position = random.choice(y_positions)
    new_turtle.goto(x=-230, y=random_y_position)
    y_positions.remove(random_y_position)
    all_turtles.append(new_turtle)

race_track = turtle.Turtle()
race_track.hideturtle()
race_track.pensize(5)
race_track.speed("fast")
start_track = (-250, -150)
for y_track in range(7):
    race_track.penup()
    race_track.goto(start_track[0], start_track[1] + (50 * y_track))
    race_track.pendown()
    race_track.forward(screen.window_width())

if user_bet:
    is_race_on = True

while is_race_on:
    for tur in all_turtles:
        if tur.xcor() > 230:
            is_race_on = False
            # print(turtle.color())  # color() method returns both the pencolor and fillcolor
            winning_turtle = tur.fillcolor()
            if winning_turtle == user_bet.lower():
                print(f"You won! The {winning_turtle} is the winner!")
            else:
                print(f"You lost! The {winning_turtle} is the winner!")
        random_distance = random.randint(0, 10)
        tur.forward(random_distance)

screen.exitonclick()
