from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

BOARDER = 290

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Score()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect snake collision with food
    if snake.head.distance(food) < 15:  # Distance method can check (x,y) or another turtle instance
        food.refresh()
        snake.extend()
        scoreboard.increase_score(point=1)

    # Detect snake collision with wall
    # if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    #     game_is_on = False
    #     scoreboard.game_over()
    if snake.head.xcor() > BOARDER:
        snake.wall_teleport_x(-BOARDER)
    elif snake.head.xcor() < -BOARDER:
        snake.wall_teleport_x(BOARDER)
    if snake.head.ycor() > BOARDER:
        snake.wall_teleport_y(-BOARDER)
    elif snake.head.ycor() < -BOARDER:
        snake.wall_teleport_y(BOARDER)

    # Detect snake head collision with snake tail collision
    # if the head collides with any segment in the tail
    # trigger game over sequence
    for segment in snake.segments[1:]:  # [1:] is slicing hence no need tp check if segment is head (segment[0])
        # if segment == snake.head:
        #     pass
        # elif snake.head.distance(segment) < 10:
        #     game_is_on = False
        #     scoreboard.game_over()
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
