import random
from turtle import Turtle
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]



class Car(Turtle):
    """ Class: Car. Creates a car of the car_color color at the (x,y) position"""

    def __init__(self, car_color, x, y):
        self.car_color = car_color
        self.x = x
        self.y = y
        super().__init__()  # crea un objeto de la clase padre Turtle
        self.shape('square')  # La forma del objeto sera un cuadrado que tendra un tamaño de 20 x 20
        self.shapesize(stretch_len=3)  # Para convertir el cuadrado en un rectangulo de 100 de largo (5 x 20)
        self.color(self.car_color)  # determina el color del cuadrado que sera parametrizado en el constructor
        self.penup()
        self.goto(self.x, self.y)
        self.setheading(180)

    def move(self):
        """ Move the car from the most right position to the most left"""
        self.speed(1)
        if self.xcor() > -300:
            self.forward(20)

        else:
            self.goto(self.x, self.y)
            self.color(random.choice(COLORS))

