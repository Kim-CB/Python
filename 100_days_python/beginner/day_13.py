# Debugging
import random

import maths


def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


from random import randint

dice_images = ["1","2","3","4","5","6"]
dice_num = randint(0, 5)

# year = int(input("What's your year of birth?"))
# if year >= 1980 and year <= 1994:
#     print("You are a millenial.")
# elif year > 1994:
#     print("You are a Gen Z.")

# try:
#     age = int(input("How old are you?"))
# except ValueError:
#     print("Type a number, strings are not acceptable.")
#     age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")
# Print is your friend
# word_per_page = 0
# pages = int(input("Number of pages: "))
# print(pages)
# word_per_page = int(input("Number of words per page: "))
# print(word_per_page)
# total_words = pages * word_per_page
# print(total_words)

# Class on Debugger
def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item)
    print(b_list)

#mutate([1, 2, 3, 5, 8, 13])

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 4000 == 0:
                return True
        else:
            return True
    else:
        return False

def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 5 == 0:
            print("Buzz")
        elif number % 3 == 0:
            print("Fizz")
        else:
            print(number)
print(fizz_buzz(8))