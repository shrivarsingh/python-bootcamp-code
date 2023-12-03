from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("Black")
screen.setup(width=800, height=600)
screen.title("Pong [Press \"SPACEBAR\" to quit]")
screen.tracer(0)  # Turn off animation

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


def stop_game():
    global game_is_on
    game_is_on = False


screen.listen()
screen.onkeypress(fun=r_paddle.go_up, key="Up")
screen.onkeypress(fun=r_paddle.go_down, key="Down")
screen.onkeypress(fun=l_paddle.go_up, key="w")
screen.onkeypress(fun=l_paddle.go_down, key="s")
screen.onkeypress(fun=stop_game, key="space")

game_is_on = True
direction = 1
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()  # Updates screen after a delay so we don't see goto animations
    ball.move()
    
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Needs to bounce
        ball.bounce_y()
    
    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()
    
    # Detect L paddle misses
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()
