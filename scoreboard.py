from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.scoreboard_update()


    def scoreboard_update(self) -> object:
        self.color('black')
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write(f"Level {self.level}", align='center', font=FONT)
