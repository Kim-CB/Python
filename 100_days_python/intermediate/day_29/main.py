from tkinter import *  # type: ignore # noqa: I001
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    #print(f"Your password is: {password}")

    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    email = email_input.get()
    password = password_input.get()
    website = website_input.get()

    if len(email) == 0 or len(password) == 0 or len(website) == 0:
        messagebox.showinfo(title="Oops",message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                                "\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as senhas:
                    senhas.write(f"{website} | {email} | {password}\n")
                    website_input.delete(0, END)
                    password_input.delete(0, END)
    
        

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Website entry
website_label = Label(text="Website: ")
website_label.grid(column=0,row=1)
website_input = Entry(window, width=35)
website_input.focus()
website_input.grid(column=1,row=1,columnspan=2)

# Email 
email_label = Label(text="Email/Username: ")
email_label.grid(column=0,row=2)
email_input = Entry(window, width=35)
email_input.insert(0, "kim______@gmail.com")
email_input.grid(column=1,row=2,columnspan=2)

# Password
password_label = Label(text="Password: ")
password_label.grid(column=0,row=3)
password_input = Entry(window, width=21)
password_input.grid(column=1,row=3)

# Button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2,row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)
window.mainloop()