# Day 26 - Intermediate - List Comprehension and the NATO Alphabet
import random

# How to create List Comprehension

numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
# is transforming this 4 lines of code in one like this:
# new_list = [new_item for item in list]
new_list = [n+1 for n in numbers]

# List Comprehensions can work with other then number, like strings
name = "Angela"
new_list = [letter for letter in name]

# Conditional List Comprehension 
# new_list = [new_item for item in list if test]
names = ["Alex","Beth", "Caroline", "Dave", "Elanor", "Freddie"]

# checking conditionaly for a name with 4 or less char in names list
# first goes through a list of names, checks for each of those names for it's lenght and if its less than five adds to this new list
short_names = [name for name in names if len(name)<5]

# Challenge
# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line. 
# You are going to create a list called result which contains the numbers that are common in both files. 

with open('file1.txt','r') as file1, open('file2.txt', 'r') as file2:
    file_ = [int(row) for row in file1]
    file__ = [int(row) for row in file2]

result = [item for item in file_ if item in file__]
#result = list(set(file_).intersection(file__))
#print(result)
# -------------------------------------------------------------------------------------------------------------
# Dictionary Comprehension
# new_dict = {new_key:new_value for item in list}
# one step further
# # new_dict = {new_key:new_value for (key, value) in dict.items()}
# one step further with condition
# # new_dict = {new_key:new_value for (key, value) in dict.items() if test}
students_scores = {student:random.randint(1,100) for student in names}
#print(students_scores)

#passed_students = {students for students in students_scores if students_scores[students] > 60}
passed_students = {students:score for (students, score) in students_scores.items() if score >= 60}

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for (word) in sentence.split()}
#print(result)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f =  {day:(temp_c*9/5)+32 for (day, temp_c) in weather_c.items()}

#print(weather_f)

# How to iterate over a Pandas DataFrame

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# for (key, value) in student_dict.items():
#     print(value)
#     print(key)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(value)
#     print(key)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)

# {new_key:new_value for (index, row) in df.iterrows()}

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}