from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

# Create the screen for the game

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()

# prepare the screen to listen for inputs from keyboard
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

screen.onkey(left_paddle.go_up, "W")
screen.onkey(left_paddle.go_down, "S")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()
