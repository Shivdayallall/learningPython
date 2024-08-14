import turtle
import pandas

screen = turtle.Screen()
screen.title("US STATE GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guess_states = []

while len(guess_states) < 50:
    # get an input from the user
    answer_state = screen.textinput(title=f"{len(guess_states)}/50 Guess The State", prompt="State Name").title()

    # get the data fromm the csv file
    state_data = pandas.read_csv("50_states.csv")

    # turn the state data into a list. this allows us to use the in key word when we iterate over the list
    all_states = state_data.state.to_list()

    if answer_state == "Exit":
        missing_states = []
        for state_data in all_states:
            if state_data not in guess_states:
                missing_states.append(state_data)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # check to see if the answer the user enter is one of the states from the csv file
    if answer_state in all_states:
        # if so create a turtle to write the name on the map
        guess_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        data_to_plot = state_data[state_data.state == answer_state]
        t.goto(data_to_plot.x.item(), data_to_plot.y.item())
        t.write(answer_state)

# this prevents  the terminal from closing on click
# turtle.mainloop()

# This function allows us to get the location on the turtle screen with each mouse click
# However we don't need it since it's already in the csv file.
# def get_mouse_click_coor(x,y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
