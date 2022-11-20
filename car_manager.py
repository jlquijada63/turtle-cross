from car import Car
import random
import time


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        for i in range(4):
            new_color = random.choice(COLORS)
            new_car = Car(new_color, 280, i * 40)
            self.cars.append(new_car)

    def move_cars(self):
        car_selected = random.choice(self.cars)
        car_selected.move()

