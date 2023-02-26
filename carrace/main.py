from turtle import Screen, Turtle
from player import Player
from car import Car
from scoreboard import Scoreboard
import time
"""
the car race programn for racing cars, 
use the UP key to move the turtle upward, if turtle reaches the final point, it returns
to it's starting position 
"""
screen= Screen()
screen.tracer(0)
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.title("Turtle car Racing")
my_player=Player()
this_car=Car()
my_score= Scoreboard()
screen.listen()
screen.onkeypress(my_player.go_up, "Up")
game_on=True
while game_on:
    time.sleep(0.1)
    screen.update()
    this_car.all_car()
    this_car.move_car()
    if my_player.ycor()>280:
        my_player.begin_position()
        my_score.call()
        this_car.move_speed()
    for car in this_car.my_car:
        if car.distance(my_player)<30 :
            with open("scope.txt", mode="w") as file:
                file.write(f"{my_score.overall()}")
            this_car.zero()
            my_score.reset()
            my_score.call()
            my_player.goto(-50,-280)
            
screen.exitonclick()