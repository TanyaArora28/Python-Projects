from turtle import Screen
from player import Player
from car_manager import Car
from score_board import Scoreboard
import time

my_screen = Screen()
my_screen.setup(height=600, width=600)
my_screen.tracer(0)

player = Player()
car_manager = Car()
score = Scoreboard()
my_screen.listen()
my_screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    my_screen.update()

    car_manager.create_cars()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            score.game_over()
            game_is_on = False

    while player.finish():
        player.go_to_start()
        car_manager.level_up()
        score.increment_level()


my_screen.exitonclick()
