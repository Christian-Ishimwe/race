from turtle import Turtle
MOVE_POSITION=(-50,-280)
DISPLACE_DISTANCE=10
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.goto(MOVE_POSITION)
        self.shape("turtle")
        self.setheading(90)
    def go_up(self):
        self.forward(DISPLACE_DISTANCE)
    def begin_position(self):
        self.goto(MOVE_POSITION)
    