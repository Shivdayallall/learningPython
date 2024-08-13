from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreBoard import ScoreBoard

# Create the screen for the game

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
score_board = ScoreBoard()

# prepare the screen to listen for inputs from keyboard
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect ball collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect ball collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if ball goes beyond the paddle

    # Detect if ball goes beyond the right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.left_point()

    # Detect if ball goes beyond the left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.right_point()

screen.exitonclick()
