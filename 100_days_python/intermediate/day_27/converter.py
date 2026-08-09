import tkinter as tk
from tkinter import messagebox, ttk

# --- Functions ---

def update_labels():
    """Updates the labels instantly when a new radio button is selected."""
    choice = radio_state.get()
    
    if choice == 1:
        from_text.config(text="Miles")
        to_text.config(text="Km")
    elif choice == 2:
        from_text.config(text="Kg")
        to_text.config(text="Lbs")
    else:
        from_text.config(text="Celsius")
        to_text.config(text="Fahrenheit")
        
    # Reset the result text when switching units
    number_text.config(text="0")
    entry.delete(0, tk.END)

def converter():
    """Calculates the conversion and catches invalid text inputs."""
    try:
        value = float(entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        return

    choice = radio_state.get()

    if choice == 1: # Mile to Km
        result = round(value * 1.60934, 2)
    elif choice == 2: # Kg to Lbs 
        result = round(value * 2.20462, 2)
    else: # Celsius to Fahrenheit
        result = round(value * (9 / 5) + 32, 2)

    number_text.config(text=f"{result}")

# --- UI Setup ---

window = tk.Tk()
window.title("Universal Unit Converter")
window.geometry("400x250")
window.config(padx=30, pady=30)

# Make the grid expand nicely
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

# Base Font
app_font = ("Arial", 11)
bold_font = ("Arial", 12, "bold")

# --- Widgets ---

# Radio buttons
radio_state = tk.IntVar(value=1)

radio_frame = ttk.Frame(window)
radio_frame.grid(column=0, row=0, rowspan=3, sticky="w")

radio_button1 = ttk.Radiobutton(radio_frame, text="Miles to Km", value=1, variable=radio_state, command=update_labels)
radio_button2 = ttk.Radiobutton(radio_frame, text="Kg to Lbs", value=2, variable=radio_state, command=update_labels)
radio_button3 = ttk.Radiobutton(radio_frame, text="Celsius to Fahrenheit", value=3, variable=radio_state, command=update_labels)

radio_button1.pack(anchor="w", pady=2)
radio_button2.pack(anchor="w", pady=2)
radio_button3.pack(anchor="w", pady=2)

# Entry
entry = ttk.Entry(window, width=12, justify='center', font=app_font)
entry.grid(column=1, row=0, padx=10)

# Labels
from_text = ttk.Label(window, text="Miles", font=app_font)
from_text.grid(column=2, row=0, sticky="w")

equal_text = ttk.Label(window, text="is equal to", font=app_font)
equal_text.grid(column=0, row=3, pady=25, sticky="e")

number_text = ttk.Label(window, text="0", font=bold_font)
number_text.grid(column=1, row=3, pady=25)

to_text = ttk.Label(window, text="Km", font=app_font)
to_text.grid(column=2, row=3, pady=25, sticky="w")

# Button
button = ttk.Button(window, text="Calculate", command=converter)
button.grid(column=1, row=4)

# --- Main Loop ---
window.mainloop()