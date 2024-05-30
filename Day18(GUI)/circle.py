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


timmy_turtle.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy_turtle.color(random_color())
        timmy_turtle.circle(200)
        timmy_turtle.setheading(timmy_turtle.heading() + size_of_gap)


draw_spirograph(5)











screen = Screen()
screen.exitonclick()
