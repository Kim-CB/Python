# Day 8 - Caesar Cipher


# Functions that allows for inputs

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

#greet_with_name("Angela")


def life_in_weeks(semana):
    year = semana
    weeks_lived = year*52
    total_weeks = 4680
    answer = total_weeks - weeks_lived
    print(f"Você tem {answer} semanas até seus 90 anos.")

#life_in_weeks(56)

#
def greet_with(name, location):
    print(f"Hello, {name}")
    print(f"What is it like in {location}")

# Positional Argument
#greet_with("Kim", "Rio de Janeiro")
# Keyword Arguments
#greet_with(location="Nowhere", name="Jack Bauer")

def calculate_love_score(name1, name2):
    true_count = 0
    love_count = 0
    true_word = "true"
    love_word = "love"
    for char in name1:
        if char in true_word:
            true_count += 1
        if char in love_word:
            love_count += 1
    for char in name2:
        if char in true_word:
            true_count += 1
        if char in love_word:
            love_count += 1
    print(f"{true_count}{love_count}")
#calculate_love_score("Angela Yu", "Jack Bauer")
import string



def caeser_cypher():
    alphabet  = list(string.ascii_lowercase)
    game_over = False

    def encrypt(original_text, shift_amount):
        cipher = ""
        for char in original_text:
            if char in alphabet:
                position = (alphabet.index(char) + shift_amount) % len(alphabet)
                cipher += alphabet[position]
            else:
                cipher += char
        print(f"Here's the encode result: {cipher}")
    
    def decrypt(original_text, shift_amount):
        cipher = ""
        for char in original_text:
            if char in original_text:
                position = (alphabet.index(char) - shift_amount) % len(alphabet)
                cipher += alphabet[position]
            else:
                cipher += char
        print(f"Here's the decode result: {cipher}")

    
    while not game_over:

        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type yout message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        if direction == "encode":
            encrypt(text, shift)
        elif direction == "decode":
            decrypt(text, shift)
        else:
            print("Invalid input. Please type 'encode' or 'decode'.")
            continue
            
        game = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

        if game == "no" or game == "n":
            print("Thank you for playing.")
            game_over = True
    
        

