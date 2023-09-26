from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xmove = 10
        self.ymove = 10

    def move(self):
        new_xcor = self.xcor() + self.xmove
        new_ycor = self.ycor() + self.ymove
        self.goto(new_xcor,new_ycor)

    def bounce(self):
        self.ymove *= -1

    def bouncePaddle(self):
        self.xmove*= -1
