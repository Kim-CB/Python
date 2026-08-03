# Day 20 - Intermediate - Build the Snake Game Part 1: Animation & Coordinates
import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

# -- Screen Config --
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Initialize
snake = Snake()
food = Food()
scoreboard = Scoreboard()
# Control the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# -- Main Game Loop
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
# Day 21 - Intermediate - Build the Snake Game Part 2: Inheritance & List Slicing
# Detect collision with food / Create a scoreboard / Detect collision with wall /Detect collision with tail
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.xcor() <-280:
        game_is_ons = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()