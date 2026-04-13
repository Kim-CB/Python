
# Day 3 - Beginner - Control Flow and Logical Operators


def module():

    number = int(input("Type a number: "))
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")


def pizza_delivery():
    print("Welcome to Python Pizza Deliveries")
    size = input("What size do you want? S, M or L: ")
    pepperoni = input("Do you wnat pepperoni on your pizza? Y or N: ")
    extra_cheese = input("Do you want extra cheese? Y or N: ")
    pizza = int()
    
    if size == "S":
        pizza += 15
    elif size == "M":
        pizza += 20
    elif size == "L":
        pizza += 25
    else:
        print("Typed something wrong.")
    
    if pepperoni == "Y" and size == "S":
        pizza += 2
    elif pepperoni == "Y" and (size == "M" or size == "L"):
        pizza += 3
    
    if extra_cheese == "Y":
        pizza += 1
    

    print("Your pizza price is:", pizza)

def age_ticket():
    print("Welcome to the RollerCoaster!")
    height = int(input("What is your height in cm? "))
    bill = 0

    if height >= 120:
        print("You can ride the rollercoaster!")
        age = int(input("What is your age?"))
        if age < 12:
            bill = 5
            print("Child tickets are $5.")
        elif age <= 18:
            bill = 7
            print("Youth tickets are $7.")
        elif 45 <= age <= 55:
            bill = 0
            print("Old mfks ride for free.")
        else:
            bill = 12
            print("Adult tickets are $12.")
        wants_photo = input("Do you want a photo taken? Y or N. ")
        if wants_photo == "Y":
            bill += 3
        print(f"Your final bill is ${bill}")
    else:
        print("Sorry, you have to grow taller before you can ride.")

age_ticket()

    


def adventure_game():
    
    print("Welcome to Tresure Island.")
    print("Your mission is to find the treasure.")
    cross_road = input("Your at a cross road. Where do you want to go?" \
    "Type 'left' or 'right'\n").lower()
    if cross_road == 'left':
        print("You've come to a lake. There is an island in the middle of the lake." )
        boat = input("Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
        if boat == "wait":
            print("You arrive at the island unharmed. There is a house with 3 doors.")
            door = input("One red, onw yellow and one blue. Which color do you choose?\n").lower()
            if door == "red":
                print("It's a room full of fire. Game Over")
            elif door == "blue":
                print("You enter a room of beasts. Game Over")
            elif door == "yellow":
                print("You found the treasure! You win!")
        elif boat == "swim":
            print("You get attacked by an angry trout. Game Over.")
    elif cross_road == 'right':
        print("You fell into a hole. Game Over.")

