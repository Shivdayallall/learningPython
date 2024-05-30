import random
import turtle
from turtle import Turtle, Screen

timmy_turtle = Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# timmy_turtle.shape("turtle")
# timmy_turtle.color("blue")
# create a square using the turtle
def create_square():
    for _ in range(4):
        timmy_turtle.forward(100)
        timmy_turtle.left(90)


# create_square()


# draw a dotted line
def draw_dotted_line():
    for _ in range(15):
        timmy_turtle.forward(20)
        timmy_turtle.penup()
        timmy_turtle.forward(20)
        timmy_turtle.pendown()


# draw_dotted_line()

colors = ["deep pink", "dark olive green", "chartreuse", "slate gray", "sienna", "yellow", "red", "purple", "cyan",
          "dodger blue", "dark cyan"]
directions = [0, 90, 180, 270]
timmy_turtle.pensize(15)
timmy_turtle.speed("fastest")


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy_turtle.forward(100)
        timmy_turtle.right(angle)


# for shape_in_side in range(3, 11):
#     timmy_turtle.color(random.choice(colors))
#     draw_shape(shape_in_side)


def random_walk():
    for _ in range(200):
        timmy_turtle.color(random_color())
        timmy_turtle.forward(30)
        timmy_turtle.setheading(random.choice(directions))


random_walk()

screen = Screen()
screen.exitonclick()
