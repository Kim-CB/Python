# Day 15 - Coffee Machine Project
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resources(command):
    sufficient_water = resources["water"] - MENU[command]["ingredients"]["water"]
    sufficient_milk = resources["milk"] - MENU[command]["ingredients"]["milk"]
    sufficient_coffee = resources["coffee"] - MENU[command]["ingredients"]["coffee"]
    if sufficient_water < 0:
        print("Sorry there is not enough water.")
        return False
    elif sufficient_milk < 0:
        print("Sorry there is not enough milk.")
        return False
    elif sufficient_coffee < 0:
        print("Sorry there is not enough coffee.")
        return False
    else: return True # Returns True if all resources are sufficient

def payment():
    pay = 0
    coins = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01,
    }
    while True:
        coins_inserted = input("Insert coins(quarters/dimes/nickels/pennies) - if is over type end : ").lower()
        # Checking for the exit first
        if coins_inserted == "end":
            return pay
        # Check if the coin is valid
        elif coins_inserted in coins:
            quantity_str = input(f"How many {coins_inserted}? ")
            # Check if the user actually typed a number
            if quantity_str.isdigit():
                # Convert the string to an integer and multiply by the specific coin's value
                quantity = int(quantity_str)
                pay += quantity * coins[coins_inserted]
            else: print("Just numbers accepted.")
        # Not 'end' and not valid coin
        else:
            print("That type of coin doesn't exist.")

def check_payment(command, pay):
    cost = MENU[command]["cost"]
    if cost > pay:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        change = round(pay - cost, 2)
        print(f"Here is ${change} in change.")
        return True

def make_coffe(command):
    water = MENU[command]["ingredients"]["water"]
    milk = MENU[command]["ingredients"]["milk"]
    coffee = MENU[command]["ingredients"]["coffee"]

    resources["water"] -= water
    resources["milk"] -= milk
    resources["coffee"] -= coffee

    print(f"Here's your {command} ☕. Enjoy!")

def main():
    print("Welcome to the Coffee Software ☕")
    money = 0
    on = True
    while on:
        command = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if command == "report":
            print(f"{resources['water']}ml\n{resources['milk']}ml\n{resources['coffee']}g\nMoney: ${money}")

        elif command == "off":
            print("Coffee Machine off.")
            on = False
        elif command in ["latte", "cappuccino", "espresso"]:
            # 1. Check if we can make it
            can_make = check_resources(command)
            if can_make:
                # 2. If we can, process payment (assign the return value to 'pay')
                pay = payment()
                # 3. Check the payment and update the machine's money 
                transaction_sucessful = check_payment(command, pay)
                # 4. Making the coffee (if payment was sucessful)
                if transaction_sucessful:
                    money += MENU[command]["cost"] # Add to machine's profit
                    make_coffe(command) # Deduct resources and serve

        else: print("Invalid input. Please choose a valid command.")

main()