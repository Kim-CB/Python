import pandas as pd

#TODO 1. Create a dictionary in this format:

alphabet_df = pd.read_csv("nato_phonetic_alphabet.csv")
alphabet_dic = {row.letter: row.code for index,row in alphabet_df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
question_on = True 
while question_on:
    question = input('Enter a word (exit to exit): ').upper()

    if question == "EXIT":
        question_on = False
    else:
        question_l = [char for char in question]
        print(question_l)

        #form_code = [code for char,code in alphabet_dic.items() if char in question_l]
        form_code = [alphabet_dic[char] for char in question_l if char in alphabet_dic]
        print(form_code)

# Course code        

# import

data = pd.read_csv("nato_phonetic_alphabet.csv")
# TODO-1
phonetic_dict = {row.letter: row.code for (index,row) in data.iterrows()}
#print(phonetic_dict)

# TODO-2
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)