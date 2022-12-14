from turtle import Turtle



STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()  # crea un objeto de la clase padre -Turtle-
        self.shape('turtle')
        self.color('red')
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

        self.level = 1

    def move(self):
        if self.ycor() <= FINISH_LINE_Y:
            self.forward(MOVE_DISTANCE)
        else:
            self.goto(STARTING_POSITION)
            self.level += 1
