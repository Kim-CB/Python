# Scope & Number Guessing Game
from random import randint


# My top of head code || Have to focus more in separating in functions
def game():
    lives = 0
    number = randint(1, 100)
    print("Welcome to the Number Guessing Game!\n" \
    "I'm thinking of a number between 1 and 100.\n")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        lives = 10
        print(f"You have {lives} attemps remainig to guess the number.")
    elif difficulty == "hard":
        lives = 5
        print(f"You have {lives} attemps remainig to guess the number.")
    else: print("Has to choose 'easy' or 'hard'.")

    game_over = False
    while not game_over:
        guess = int(input("Make a guess: "))
        if guess > number:
            lives -= 1
            print("Too high.\nGuess again.")
            print(f"You have {lives} attemps remainig to guess the number.")
        if guess < number:
            lives -= 1
            print("Too low.\nGuess again.")
            print(f"You have {lives} attemps remainig to guess the number.")
        if lives == 0:
            print("You ran out of guesses. You lose.")
            game_over = True
        if guess == number:
            print(f"Congratulations you guessed correctly. The number was {number}.")
            game_over = True


# Course Version
#

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("Too high.")
        return turns-1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns-1
    else: print(f"You got it! The answer was {actual_answer}")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard'.")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def course_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    turns = set_difficulty()
    print(f"You have {turns} attemspts remaining to guess the number.")
    guess= 0
    while guess != answer:
        print(f"You have {turns} attemspts remaining to guess the number.")
        # The user guesses
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You ran out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")



