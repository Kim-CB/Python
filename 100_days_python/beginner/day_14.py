# Higher or Lower
# imports 
import random

from higher_lower_art import logo, vs
from higher_lower_data import data

# Breakdown the problem
data_list = data
# simple game(made in night) 40 min - only my head
def game():
    print(logo)
    points = 0
    should = True
    first = random.choice(data_list)
    second = random.choice(data_list)
    while should:
            if first['follower_count'] > second['follower_count']:
                winner = 'a'
            else: winner = 'b'
            print(f"Compare A: {first["name"]}, {first["description"]}, from {first["country"]}.")
            print(vs)
            print(f"Against B: {second["name"]}, {second["description"]}, from {second["country"]}.\n")
            choose = input("Who has more followers? Type 'A' or 'B': ").lower()
            if choose == winner:
                points += 1
                print(f"You're right! Current score: {points}")
                if winner == "b":
                    first = second
                    second = random.choice(data_list)
                else: second = random.choice(data_list)
            if choose != 'a' and choose != 'b':
                 print("Write A or B.")
            else: 
                print(f"Sorry, that's wrong. Final score: {points}")
                should = False


# Solution from the course    


def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower counts and returns if they got it right"""
    if a_followers > b_followers:
        return user_guess == "a"
    else: return user_guess == "b"


# Display art
print(logo)
score = 0

# Make the game repeatable.

game_should_continue = True
account_b = random.choice(data)
while game_should_continue:
    # Generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clear the screen
    print("\n"*50)
    print(logo)

    # Check if user is correct
    # - Get a follower count of each account 
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess.
    # score keeping
    if is_correct:
        score += 1
        print("You're right! Current score {score}")
    else:
        print("Sorry, that's wrong. Final score {score}")
        game_should_continue = False

    # Making account at position B become the next account at position A.