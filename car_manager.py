from turtle import Turtle
import random
import time


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10





class CarManager(Turtle):
    def __init__(self, starting_position):
        self.starting_position = starting_position
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=5)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(300, self.starting_position)
        self.setheading(180)


    def move(self):
        while self.xcor() > -300:
            self.speed(1)
            self.forward(MOVE_INCREMENT)






