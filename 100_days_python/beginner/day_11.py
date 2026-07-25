# Blackjack

import random

def deal_card():
    """Returns a random card from a theoretically infinite deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(hand):
    """Check for a blackjack (a hand with only 2 cards: an ace and a 10)"""
    if sum(hand) == 21 and len(hand) == 2:
        return 0 # 0 will represent a Blackjack
    # If they are over 21 but have an Ace, change the Ace (11) to a 1
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)

    return sum(hand)

def compare(user_score, cpu_score):
    if user_score == cpu_score:
        return "It's a tie!🙃"
    elif cpu_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over 21. You lose 😭"
    elif cpu_score > 21:
        return "Dealer busted. You win! 😁"
    elif user_score > cpu_score:
        return "You win! 😃"
    else:
        return "You lose 😤"
    

def blackjack():
    # Initialize hands inside the function so you can play multiple rounds
    player_card = [deal_card(), deal_card()]
    dealer_card = [deal_card(), deal_card()]
    dealer_score = -1
    player_score = -1

    is_game_over = False
    # Player Turn
    while not is_game_over:
        player_score = calculate_score(player_card)
        dealer_score = calculate_score(dealer_card)

        print(f"\nYour hand: {player_card}, current score: {player_score}")
        # Standart rule: Only show the dealer's first card to the player
        print(f"Dealer's first card: {dealer_card[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if choice == 'y':
                player_card.append(deal_card())
            elif choice == 'n':
                is_game_over = True
            else: print("Invalid choice. Please type 'y' or 'n'.")

    # Dealer's Turn

    if player_score != 0 and player_score <= 21:
        while dealer_score != 0 and dealer_score < 17:
            dealer_card.append(deal_card())
            dealer_score = calculate_score(dealer_card)

    print("\n" + "="*20)
    print(f"Final Cards - Player: {player_card} | Score: {player_score}")
    print(f"Final Cards - Dealer: {dealer_card} | Score: {dealer_score}")
    print("="*21 + "\n")
    print(compare(player_score, dealer_score))




# Main Game 
print("-"*50)
print(" "*5,"Welcome to Blackjack"," "*5)
print("-"*50)
print("Blackjack is a card game where the user goes against the dealer.")
print("Your goal is to draw cards to get closest to 21 points, however you don't want to go above 21 points because you will lose!")

while True:
    play = input("Would you like to play a game of Blackjack? (y/n): ").lower()
    if play == "y":
        blackjack()
    elif play == "n":
        print("-"*20)
        print("Thank you for playing. Goodbye!")
        break
    else: print("You did not enter either 'y' or 'n'.")