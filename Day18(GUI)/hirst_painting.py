import random
import turtle
from turtle import Turtle, Screen
# import colorgram
#
#

# rgb_colors = []
# colors = colorgram.extract("cta-imh.png", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
#
#
# print(rgb_colors)
color_list = [(250, 249, 248), (231, 196, 131), (238, 240, 239), (219, 154, 100), (78, 164, 212), (213, 225, 233), (34, 42, 79), (59, 105, 155), (194, 93, 136), (97, 111, 191), (200, 124, 172), (119, 194, 185), (213, 102, 94), (46, 57, 91), (232, 219, 224), (45, 151, 206), (130, 79, 127), (166, 194, 221), (121, 92, 78), (59, 46, 57), (62, 53, 48), (162, 203, 215), (213, 176, 196), (222, 180, 167), (78, 54, 73), (158, 128, 92), (72, 65, 52), (56, 59, 57), (95, 109, 105), (81, 56, 50)]

timmy_turtle = Turtle()
turtle.colormode(255)
timmy_turtle.speed("fastest")
timmy_turtle.penup()
timmy_turtle.hideturtle()
timmy_turtle.setheading(225)
timmy_turtle.forward(300)
timmy_turtle.setheading(0)
number_of_dot = 100

for dot_count in range(1, number_of_dot + 1):
    timmy_turtle.dot(20, random.choice(color_list))
    timmy_turtle.forward(50)

    if dot_count % 10 == 0:
        timmy_turtle.setheading(90)
        timmy_turtle.forward(50)
        timmy_turtle.setheading(180)
        timmy_turtle.forward(500)
        timmy_turtle.setheading(0)














screen = Screen()
screen.exitonclick()