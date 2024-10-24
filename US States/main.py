import turtle
import pandas
screen = turtle.Screen()
screen.title("US States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer = screen.textinput(title=f"{len(guessed_state)}/50 States",prompt="Enter a state name").title()
    if answer == "Exit":
        missing_states = []
        for state in states:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer in states:
        guessed_state.append(answer.title())
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state==answer]
        t.goto(state_data["x"].item(),state_data["y"].item())
        t.write(state_data.state.item())
