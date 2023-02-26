from turtle import Turtle
import random
COLOR=["red","blue","black","yellow"]
INCREMENT_SPEED=3

class Car(Turtle):
    def __init__(self):
        self.my_car=[]
        self.my_speed=INCREMENT_SPEED
    def all_car(self):
        chance_car=random.randint(0, 6)
        if chance_car==1:
            new_car=Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.color(random.choice(COLOR))
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            random_y=random.randint(-240, 240)
            new_car.goto(300,random_y)
            self.my_car.append(new_car)
    def move_car(self):
        for join in self.my_car:
           join.backward(self.my_speed)
    def  move_speed(self):
        self.my_speed+=1
    def zero(self):
        for can in self.my_car:
            can.goto(1000,1000)
        self.my_car.clear()
        self.all_car()

