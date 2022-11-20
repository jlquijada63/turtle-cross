from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from car import Car
from scoreboard import Scoreboard


# creando la pantalla inicial

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.title("Turtle-crossing")
screen.tracer(0)

screen.listen()

player = Player()

car_manager = CarManager()

scoreboard = Scoreboard()

screen.onkey(player.move, 'Up')

scoreboard.level = player.level

play_is_on = True

while play_is_on:
    time.sleep(0.1)
    car_manager.move_cars()
    scoreboard.scoreboard_update()
    screen.update()



screen.exitonclick()
