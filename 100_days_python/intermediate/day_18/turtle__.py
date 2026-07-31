# Day 18 - Intermediate - Turtle & the Graphical User Interface
from random import choice, random
from turtle import Screen, Turtle

tim = Turtle()
#tim.shape('triangle')

#Challenge 1 - Draw a Square
def chag1():
    while True:
        tim.forward(100)
        tim.left(90)
        if abs(tim.pos()) < 1:
            break

#Challenge 2 - Draw a Dashed Line
#i did a dashed square
def chag2():
    while True:
        for _ in range(9):
            tim.forward(10)
            tim.penup()
            tim.forward(10)
            tim.pendown()
        tim.left(90)
        if abs(tim.pos()) < 1:
            break

#Challenge 3 - Drawing Different Shapes
#Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
def random_color():
    r = random()
    g = random()
    b = random()
    random_color = (r, g, b)
    return random_color

def shape(number):
    while True:
        tim.forward(100)
        tim.left(number)
        if abs(tim.pos()) < 1:
            break

def chag3():
    for i in range(3,11):
        shape(360/i)
        tim.color(random_color())

# Challenge 4 - Draw a Random Walk
# increase thickness
def random_walk():
    directions = [0, 90, 180,270]
    for _ in range(200):
        tim.forward(50)
        tim.setheading(choice(directions))
        tim.color(random_color())
        
def chag4():
    tim.width(10)
    tim.speed("fastest")
    random_walk()

# Challenge 5 - Draw a Spirograph
def chag5():
    for i in range(1, 361):
        tim.speed("fastest")
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(i)
    

screen = Screen()
screen.exitonclick()