# Day 19 - Intermediate - Instances, State and Higher Order Functions
from random import randint
from turtle import Screen, Turtle

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet =  screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_racers = []

for i in range(0,6):  # noqa: PIE808
    new_t = Turtle(shape="turtle")
    new_t.penup()
    new_t.goto(x=-230, y=y_pos[i])
    new_t.color(colors[i])
    all_racers.append(new_t)

if user_bet:
    race_on = True

while race_on:
    for racer in all_racers:
        if racer.xcor() > 230:
            race_on = False
            win_race = racer.pencolor()
            if win_race == user_bet:
                print(f"You've won! The {win_race} turtle is the winner!")
            else:
                print(f"You've lost! The {win_race} turtle is the winner!") 
        dist = randint(0,10)
        racer.forward(dist)

screen.exitonclick()

# Expand Solutions and works