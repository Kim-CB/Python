# Day 2 - Beginner - Understanding Data Types and How to Manipulate Strings

def tip_calculator():
    print("Welcome to the tip calculator!")
    total = float(input("What was the total bill? $ "))
    tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
    people = int(input("How many people to split the bill? "))
    bill = (total + (total*(tip/100))) / people
    print("Each person should pay:", round(bill, 2))

tip_calculator()