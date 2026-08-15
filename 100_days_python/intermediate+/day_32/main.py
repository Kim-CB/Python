import datetime as dt
import smtplib
from random import randint

import pandas as pd

##################### Extra Hard Starting Project ######################

# email and password for automatic emaling
my_email = "example@gmail.com"
password = "1234565@asdf"


# making a tuple to todays day and month
current_day = dt.datetime.now().date()  # noqa: DTZ005
current_day_tuple = (current_day.month, current_day.day)

#dic = pd.read_csv("birthdays.csv", index_col=0).to_dict("dict")
# if new_day["month"] in dic['month'].values():
#     print(dic['month'].keys())

# reading csv
data = pd.read_csv("birthdays.csv")
# dic comprehension to create a dictionary from the csv that is formated like we want:
# birthday = {
#   (birthday_month, birthday_day): data_row
# }
birthday_dic = {(data_row["month"], data_row['day']):data_row for (index, data_row) in data.iterrows()}

# checking the match and sending the email using smtplib
if current_day_tuple in birthday_dic:
    birthday_person = birthday_dic[current_day_tuple]
    path = f"letter_templates/letter_{randint(1,3)}.txt"
    with open(path) as file:
        contents = file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="send_to@mail.com",
                            msg=f"Subject:Happy Birthday!\n\n{contents}")
