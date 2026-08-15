# Day 32 - Intermediate+ - Send Email(smtplib) & Manage Dates (datetime)

# Email smtplib is module defined in python library
# datetime is also a python module that helps with to define dates and times

# smtplib.SMTP("smtpl.gmail.com", port=587)
# SMTP (Simple Mail Transfer Protocol)




# starttls() - Transport Layer Security

# smtp-mail.outlook.com

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email , password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="email_i_wanna_send@mail.com",
#                         msg="Subject: Hello\n\nThis is the body of my email.")

import datetime as dt

now = dt.datetime.now()  # noqa: DTZ005
year = now.year
month = now.month
day_of_week = now.weekday
print(now)

date_of_birth = dt.datetime(year= 2001, month= 2, day= 22, hour=4)  # noqa: DTZ001
print(date_of_birth)

import datetime as dt
import smtplib
from random import choice

my_email = "email@gmail.com"
password = "129381384289"



current_day = dt.datetime.now().weekday()  # noqa: DTZ005
if current_day == 5:
    with open("quotes.txt", "r") as data:
        quotes = [line.rstrip() for line in data]
    random_quote = choice(quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email , password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="send_to@outlook.com",
                            msg=f"Subject: Motivation\n\n{random_quote}")