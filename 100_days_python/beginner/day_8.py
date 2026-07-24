# Day 8 - Caesar Cipher
import string
from caesar_art import logo
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
        print(logo)

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
#caeser_cypher()

# TODO-1 Import and print the logo form art.py when the program starts.
# TODO-2 What happens if the user enters a number/symbol/space that's not in the List alphabet

def caesar(original_text, shift_amount, encode_or_decode):
    alphabet = list(string.ascii_lowercase)
    output_text = ""
    if encode_or_decode == "decode":
                    shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode} result: {output_text}")

should_continue = True
while should_continue:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type yout message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower

    if restart == "no":
        should_continue = False
        print('Goodbye')