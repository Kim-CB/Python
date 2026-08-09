# Day 27 - Intermediate - Tkinter *args, **kwargs and Creating GUI Programs

import tkinter

# pack() will always start from the top and place the widget bellow the next one (only with you change the side=)
# place() is all about precise space, you can put a x= and y=
# grid() divides the space in a grid system

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text =new_text)

window = tkinter.Tk()
window.title("First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)

# Label

my_label = tkinter.Label(text="I Am a Label", font=('Arial', 24, 'bold'))
my_label.config(text="New Text")
my_label.grid(column=0,row=0)
my_label.config(padx=100,pady=200)


# Button

button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1,row=1)

button_2 = tkinter.Button(text="New Button")
button_2.grid(column=2,row=0)

# Entry

input = tkinter.Entry(width=10)
print(input.get())
input.grid(column=3,row=2)









window.mainloop()

