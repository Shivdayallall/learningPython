from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()

        # variable to Move the ball by 10 points in x and y direction
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # to get the ball to bounce off the wall we need it to move in opposite direction of the current direction
        # so whatever the current direction is, we will multiply it by -1 so get a negative number or positive number
        # depending on its current direction. keep in mind we only need the ball to bounce on the y position not the x
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
