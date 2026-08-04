import time
from random import randint
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

frogger = Player()
scoreboard= Scoreboard()
cars = []


screen.listen()
screen.onkey(frogger.move, key="space")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    random_chance = randint(1,6)
    if random_chance == 1:
        random_position = (300,randint(-250,250))
        cars.append(CarManager(random_position))
    for car in cars:
        car.move_car()
        # Detect collision with cars
        if car.distance(frogger) < 20:
            scoreboard.game_over()
            game_is_on = False
            print("Collision")



    if frogger.ycor() >= 285:
        scoreboard.new_level()
        frogger.goto(0,-280)
        CarManager.car_speed += 10

        print("You win")

screen.exitonclick()