# Day 4 - Beginner - Randomisation and Python Lists
import random

# Exercício Pedido do Dia
def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]


    person = input("Rock, Paper or Scissors?").lower()

    cpu = random.choice(choices)
    print("cpu escolheu...",cpu)

    if (person == "rock" and cpu == "scissors") or (person == "paper" and cpu == "rock") or (person == "Scissors" and cpu == "paper"):
        print("You win!")
    elif person == cpu:
        print("Draw")
    elif person != "rock" or "paper" or "scissors":
        print("Invalid choice, you lose!")
    else:
        print("CPU win!")

# Exercício do Dia (Versão Prof)

def rock_pap_sci():
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    
    computer_choice = random.randint(0, 2)
    print(f"Computer chose {computer_choice}")

    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number. You lose!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0  and user_choice == 2:
        print("You lose!")
    elif computer_choice > user_choice:
        print("Computer wins!")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw!")
    
    


# Listas
def listas():
    states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
    # dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
    fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
    vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
    dirty_dozen = [fruits, vegetables]
    print(dirty_dozen[1][1])
    

# 33. Who will pay the bill
def bill():
    # 1 opção
    friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
    paid = random.choices(friends)
    print(paid)
    # 2 opção
    random_index = random.randint(0,4)
    print(friends[random_index])

rock_paper_scissors()