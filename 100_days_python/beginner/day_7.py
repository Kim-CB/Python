# Day 7 - Hangman
#
#
from random import choice
from hangman_art import logo,stages
from hangman_words import word_list

def hangman():
    hangman_word = []
    chosen_word = choice(word_list)
    game_over = False
    lives = 6
    for i in range(len(chosen_word)):
        hangman_word.append("_")
    print(f"The word is {chosen_word}")

    while not game_over:
        # User input
        print(logo)
        print(f"**********{lives}/6 LIVES LEFT***********")
        guess = input("Guess a letter: ").lower()

        if guess in hangman_word:
            print(f"You've already guessed {guess}")

        # Check if user is wrong
        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            if lives == 0:
                print("You lost!")
                print(f"word was {chosen_word}")
                game_over = True
        
        # Check guessed letter
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                hangman_word[position] = guess

        # Print progress
        print(stages[lives])
        print(*hangman_word)
        
        # Check if won
        if "_" not in hangman_word:
            print("You won!")
            game_over = True
hangman()
