import turtle

import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
answers = []

while len(answers) < 50:
    answer = screen.textinput(
        title=f"{len(answers)}/50 States Correct",
        prompt="What's another state's name? (type 'Exit' to quit)"
    )

    # User closed the dialog or typed Exit
    if answer is None or answer.lower() == "exit":
        break

    answer_title = answer.title()

    # Already guessed? Skip silently
    if answer_title in answers:
        continue

    # Not in the list at all?
    if answer_title not in data["state"].values:
        continue

    # Valid guess - get that row and write the name on the map
    row = data[data["state"] == answer_title].iloc[0]
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(row["x"],row["y"])
    t.write(answer_title, align="center", font=("Arial", 8, "normal"))

    answers.append(answer_title)

# Save the states the player missed
missed = [s for s in data["state"].to_list() if s not in answers]
pd.DataFrame(missed, columns=["missed_states"]).to_csv("states_to_learn.csv")

screen.exitonclick()


