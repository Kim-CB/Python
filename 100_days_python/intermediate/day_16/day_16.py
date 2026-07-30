# Day 16 - Intermediate - Object Oriented Programming (OOP)

# from turtle import Screen, Turtle

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Pokemon Name", "Type"]
table.align = "l"
table.add_rows(
    [
        ["Pikachu", "Eletric+"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"]
    ]
)


print(table)