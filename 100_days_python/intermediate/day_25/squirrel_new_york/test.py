
# with open("weather_data.csv","r") as data_line:
#     datas = data_line.readlines()
#     print(datas)

# import csv
# dados = [1,2,3]
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas as pd

# data =pandas.read_csv("weather_data.csv")
# print(data["temp"])

# data_dic = data.to_dict()
# print(data_dic)

# temp_list = data["temp"].to_list()
# # average = sum(temp_list)/len(temp_list)
# # print(average)
# # print(data["temp"])
# # print(data["temp"].mean())

# high = data.temp.max()
# print(data[data.temp == high])

# monday = data[data.day == "Monday"]
# convert = (monday.temp[0]*1.8)+32
# print(convert)
        
# Creating dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# Squirrel Challenge
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Best Code
fur_counts = (
    data["Primary Fur Color"]
    .value_counts()
    .rename_axis("Fur Color")
    .reset_index(name="Count")
)

print(fur_counts)
fur_counts.to_csv("squirrel_fur_counts.csv", index=False)

# My Start Code
fur = data.groupby("Primary Fur Color").count()
name = fur.index.tolist()

data_dict = {
    "Fur Color":[name[0],name[1],name[2]],
    "Count":[fur.X[name[0]],fur.X[name[1]],fur.X[name[2]]]
}

df = pd.DataFrame(data_dict)
print(df)
df.to_csv("squirrel_count.csv")

# Course Code
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count_course.csv")