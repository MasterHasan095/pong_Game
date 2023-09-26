import time
from turtle import Screen
from turtle import Turtle

from ball import Ball
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

game_is_on = True

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
screen.listen()

screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # Detect Collision

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect Collision with paddle

    if (ball.distance(r_paddle) < 50 and 320 < ball.xcor()) or (
            ball.distance(l_paddle) < 50 and -320 > ball.xcor()):
        ball.bouncePaddle()

    if ball.xcor() > 380 or ball.xcor() < -380:
        gameover = Turtle()
        gameover.color("white")
        gameover.penup()
        gameover.goto(-50, 0)
        gameover.write("GAMEOVER", move=False, align="left", font=("Arial", 12, "normal"))
        game_is_on = False

screen.exitonclick()
