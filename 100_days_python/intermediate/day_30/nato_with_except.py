# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


on = True
while on:
    try: 
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
        print(output_list)
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        on = False

# Course Code

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()
