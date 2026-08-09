# Mile to Km Converter

from tkinter import *  # type: ignore


def converter():
    mile = float(input.get())
    km = round(mile*1.6, 2)
    number_text.config(text=km)
    

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200,height=100)

# Entry
input = Entry(width=10 ,justify='center')
input.grid(column=1,row=0)

# Text
miles_text = Label(text="Miles")
miles_text.grid(column=2,row=0)
equal_text = Label(text="is equal to")
equal_text.grid(column=0,row=1)
number_text = Label(text="0")
number_text.grid(column=1, row=1)
km_text = Label(text="Km")
km_text.grid(column=2, row=1)


# Button
button = Button(text="Calculate",command=converter)
button.grid(column=1,row=2)


window.mainloop()