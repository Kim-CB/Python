# Day 5 Test - Password Generator
import random
def password_generator():

    letters = [chr(i) for i in range(ord('A'), ord('Z') + 1) and range(97,123)]
    numbers = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator")
    nr_letters = int(input(f"How many letters would you like in your passsword?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    answer_list = []
    for _ in range(nr_letters):
        answer_list.append(random.choice(letters))
    for _ in range(nr_numbers):
        answer_list.append(random.choice(numbers))
    for _ in range(nr_symbols):
        answer_list.append(random.choice(symbols))
    random.shuffle(answer_list)
    answer = ''.join(answer_list)
    print(f"Here is your password:\n{answer}")
password_generator()