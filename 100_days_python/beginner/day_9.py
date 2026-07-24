# Day 9 - Secret Auction 
from auction_art import logo

def highest_bidder(bidding_record):
    # max() with key=bidding_record.get finds the key with the highest value
    highest_bid = max(bidding_record.values())

    winners = [bidder for bidder, bid in bidding_record.items() if bid == highest_bid]
    if len(winners) > 1:
        tied_names = ", ".join([name.title() for name in winners])
        print(f"It's a tie! {tied_names} all bid the highest amount of ${highest_bid}.")
    else: 
        winner = winners[0]
        print(f"The winner is {winner.title()} with a bid of ${highest_bid}")

# Initialize the empty dictionary 
bidders = {}
print(logo)

should_continue = True

while should_continue:
    # Name Validation 
    while True:
        name = input("What is your name? ").lower()
        if name.replace(" ", "").isalpha():
            name = name.lower()
            break
        else:
            print("Invalid input. Please use letters only for your name.")

    # Bid Validation 
    while True:
        try:
            bid = float(input("What is your bid? ").strip())
            if bid > 0:
                break
            else:
                print("Please enter a positive number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")
    bidders[name] = bid
    # Others Validation
    while True:
        others = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
        if others in ['yes', 'no']:
            break
        else:
            print("Please type 'yes' or 'no'.")
    if others == "no":
        should_continue = False
        # Pass the dictionary to the function once the loop is done
        highest_bidder(bidders)
    # Clears the screen by print 100 lines
    if others == "yes":
        print("\n" * 100)
        print(logo)

