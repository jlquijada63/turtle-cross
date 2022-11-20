

from turtle import Screen
import time
from player import Player
from car_manager import CarManager


# creando la pantalla inicial

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.title("Turtle-crossing")
screen.tracer(0)


screen.listen()

player = Player()
car = CarManager(0)
car.move()

screen.onkey(player.move, 'Up')

play_is_on = True


while play_is_on:
    time.sleep(0.1)
    screen.update()






screen.exitonclick()