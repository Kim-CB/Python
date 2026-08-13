# -- Better Pomodoro
import customtkinter as ctk

# -------------- App Setup -------------------
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("360x640")
app.title("Pomodoro Timer")
app.configure(fg_color="#FFF1EE")

# --------------- Variables ----------------
WORK_TIME = 1 * 60
time_left = WORK_TIME
running = False


# -------------- Functions --------------

def update_timer():
    global time_left, running
    if running and time_left >= 0:
        minutes = time_left // 60
        seconds = time_left % 60
        timer_label.configure(text=f"{minutes:02d}\n{seconds:02d}")
        time_left -= 1
        app.after(1000, update_timer)

def start_pause():
    global running
    running = not running
    if running:
        play_btn.configure(text="⏸")
        update_timer()

def reset_timer():
    global time_left, running
    running = False
    time_left = WORK_TIME
    play_btn.configure(text="▶")
    timer_label.configure(text="25\n00")

# --------------- UI -----------------

focus_label = ctk.CTkLabel(
    app,
    text="🧠 Focus",
    fg_color="#FADBD6",
    text_color="#4A1C1C",
    corner_radius=20,
    padx=20,
    pady=6,
    font=("Helvetica", 14, "normal")
)
focus_label.pack(pady=30)

# Timer
timer_label = ctk.CTkLabel(
    app,
    text="25\n00",
    font=("Helvetica", 96, "bold"),
    text_color="#3B0D0D",
    justify= "center"
)
timer_label.pack(expand=True)

# Controls
controls = ctk.CTkFrame(app, fg_color="transparent")
controls.pack(pady=40)

menu_btn = ctk.CTkButton(
    controls,
    text="...",
    width=60,
    height=60,
    corner_radius=20,
    fg_color="#FADBD6",
    hover_color= "#F2CFC9",
    text_color= "#3B0D0D",
    font=("Helvetica", 22, "bold")
)
menu_btn.grid(row=0, column=0, padx=10)

play_btn = ctk.CTkButton(
    controls,
    text="▶",
    width=80,
    height=80,
    corner_radius=28,
    fg_color="#FF7A73",
    hover_color="#FF6A63",
    text_color= "white",
    font=("Helvetica", 26, "bold"),
    command=start_pause
)
play_btn.grid(row=0, column=1, padx=10)

reset_btn = ctk.CTkButton(
    controls,
    text="⏭",
    width=60,
    height=60,
    corner_radius=20,
    fg_color="#FADBD6",
    hover_color="#F2CFC9",
    text_color="#3B0D0D",
    font=("Helvetica", 22, "bold"),
    command=reset_timer
)
reset_btn.grid(row=0, column=2, padx=10)

# Run
app.mainloop()