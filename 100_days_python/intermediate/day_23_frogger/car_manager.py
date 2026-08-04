from random import choice
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

loc = [(0,-120),(0,280)]


class CarManager(Turtle):
    car_speed = STARTING_MOVE_DISTANCE

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(choice(COLORS))
        self.turtlesize(1,2)
        self.move_car()
        self.goto(position)


    def move_car(self):
        new_x = self.xcor() - CarManager.car_speed
        self.goto(new_x, self.ycor())

    def level_up(self):
        CarManager.car_speed += MOVE_INCREMENT
