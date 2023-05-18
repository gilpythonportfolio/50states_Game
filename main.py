import pandas as pd
import turtle

data = pd.read_csv("50_states.csv")
data["state"] = data["state"].str.lower()

screen = turtle.Screen()
message_turtle = turtle.Turtle()
state_turtle = turtle.Turtle()

message_turtle.hideturtle()
message_turtle.penup()
message_turtle.goto(-300, -300)

screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Guessed", prompt="What's the next state?")
    
    if answer_state is None:
        break

    answer_state = answer_state.lower()

    if answer_state in data['state'].values:
        guessed_states.append(answer_state)
        message_turtle.clear()
        message = f"{answer_state} is in the list of states!"
        message_turtle.write(message, align="left", font=("Arial", 16, "normal"))
        
        state_data = data[data["state"] == answer_state]
        state_x = int(state_data['x'])
        state_y = int(state_data['y'])
        
        state_turtle.penup()
        state_turtle.goto(state_x,state_y)
        state_turtle.write(answer_state.title(), align="center")

    elif answer_state == 'exit':
        unguessed_states = [state for state in data["state"] if state not in guessed_states]
        new_data = pd.DataFrame(unguessed_states)
        new_data.to_csv("new.csv")
        break

turtle.mainloop()
