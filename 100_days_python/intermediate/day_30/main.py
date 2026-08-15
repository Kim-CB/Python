from tkinter import *  # type: ignore # noqa: I001
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
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
    new_data = {
        website: {
            "email":email,
            "password": password,
        }
    }

    if len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as senhas:
                # Reading old data
                data = json.load(senhas)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as senhas:
                json.dump(new_data, senhas, indent=4)
        else: 
            data.update(new_data)
            with open("data.json", "w") as senhas:
                # Saving updated data
                json.dump(data, senhas, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- SEARCH ------------------------------- #       

def find_password():
    website = website_input.get()
    try: 
        with open("data.json", "r") as data_file:
            data_check = json.load(data_file)
    except FileNotFoundError:
            print("No Data File Found")
    else:
        if website in data_check:
            messagebox.showinfo(title=f"{website}", message=f"Email: {data_check[website]["email"]}\n Password: {data_check[website]["password"]}")
            website_input.delete(0, END)
        else:
            messagebox.showinfo(title="Error", message="No details for the website exists")




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
website_input = Entry(window, width=21)
website_input.focus()
website_input.grid(column=1,row=1)

# Email 
email_label = Label(text="Email/Username: ")
email_label.grid(column=0,row=2)
email_input = Entry(window, width=35)
email_input.insert(0, "kim______@gmail.com")
email_input.grid(column=1,row=2,columnspan=2, sticky="w")

# Password
password_label = Label(text="Password: ")
password_label.grid(column=0,row=3)
password_input = Entry(window, width=21)
password_input.grid(column=1,row=3)

# Button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2,row=3, sticky="ew")

search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky="w")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)
window.mainloop()