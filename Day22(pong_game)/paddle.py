from turtle import Screen, Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        # Create the paddle for the game

        self.shape("square")
        self.color("green")
        self.shapesize(stretch_len=1, stretch_wid=5)

        # penup removes the line when the paddle moves across the screen
        self.penup()
        self.goto(position)

    # create up function to move paddle up when up button is press

    def go_up(self):
        # take the current position of the y cor and add 20 to it
        new_y_position = self.ycor() + 30
        self.goto(self.xcor(), new_y_position)

    def go_down(self):
        # take the current position of the y cor and add 20 to it
        new_y_position = self.ycor() - 30
        self.goto(self.xcor(), new_y_position)
