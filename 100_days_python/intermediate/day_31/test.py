# Capstone Project - Flash Card Program

from random import randint
from tkinter import *  # type: ignore

import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- FUNCTIONS ------------------------------- #

def read_french():
    global flip_timer, french
    window.after_cancel(flip_timer)
    with open("./data/french_words.csv", "r") as data:
        df = pd.read_csv(data).to_dict("records")
        french = df[randint(0,100)]["French"]
        canvas.itemconfig(word, text=french, fill="black")
        canvas.itemconfig(title, text="French", fill="black")
        flip_timer = window.after(3000,read_english)

def read_english():
    with open("./data/french_words.csv", "r") as data:
        df = pd.read_csv(data).to_dict("records")
        english = df[randint(0,100)]["English"]
        canvas.itemconfig(word, text=english, fill="white")
        canvas.itemconfig(title, text="English", fill="white")
        canvas.itemconfig(canvas_image, image=back_card)


def is_known():
    with open("./data/french_words.csv", "r") as data:
        df = pd.read_csv(data).to_dict("records")
        df.remove(french) 
        print(df)       
        read_english()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=70, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,read_english)


canvas = Canvas(width=1000, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
back_card = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(500,300, image= card_front)
canvas.grid(column=0, row=0,columnspan=2)

right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")
button_wrong=Button(image=wrong_img, highlightthickness=0, command=read_french)
button_wrong.grid(column=0, row=1)
button_right=Button(image=right_img, highlightthickness=0, command=is_known)
button_right.grid(column=1, row=1)

# canvas.create_image(200, 620, image=wrong_img)
# canvas.create_image(750, 620, image=right_img)

# Label
title = canvas.create_text(500,150,text="",font=("Ariel",40, "italic"))

word = canvas.create_text(500,300,text="",font=("Ariel",60, "bold"))


read_french()
window.after(3000,read_english)

window.mainloop()