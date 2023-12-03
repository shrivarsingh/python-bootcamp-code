import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def end_game():
    global game_is_on
    game_is_on = False
    screen.title("-- GAME STOPPED -- CLOSE WINDOW --")

# Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle crossing -> Press \"Up\" to move  or \"Esc\" to exit game.")
screen.listen()
screen.onkeypress(fun=end_game,key="Escape")
screen.colormode(255)

# Player
player = Player()
screen.onkeypress(fun=player.move_up,key="Up")

# Car Manager
def add_new_car():
    new_car = CarManager()
    cars.append(new_car)

cars = []
add_new_car()
car_counter = 0

# Scoreboard
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(scoreboard.level)
    screen.update()

    # Move Car
    for car in cars:
        car.move_car_across()
        if car.distance(player) < 20:
            end_game()
            scoreboard.game_over()
        if car.xcor() < -1200:
            cars.remove(car)

    # Turtle Win
    player_win = player.check_player_won()
    if player_win:
        player.starting_pos()
        scoreboard.update_score()
    
    car_counter += 1
    if car_counter % 10 == 0:
        car_counter = 0
        add_new_car()
    
screen.exitonclick()
