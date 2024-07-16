from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

# segment_1 = Turtle("square")
# segment_1.color("white")
#
# segment_2 = Turtle("square")
# segment_2.color("white")
# segment_2.goto(-20, 0)
#
# segment_3 = Turtle("square")
# segment_3.color("white")
# segment_3.goto(-40, 0)

# PROGRAMATIC WAY TO DO ABOVE TASK IS TO USE A LOOP

starting_position = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_number in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_number - 1].xcor()
        new_y = segments[seg_number - 1].ycor()
        segments[seg_number].goto(new_x, new_y)
    segments[0].forward(20)







screen.exitonclick()