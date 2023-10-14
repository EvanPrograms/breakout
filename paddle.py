from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("gray")
        self.right(90)
        self.shapesize(stretch_wid=10, stretch_len=1)
        self.penup()
        self.goto(position)
        self.move_left = False
        self.move_right = False
        self.move_speed = 1.1

    def go_left_start(self):
        self.move_left = True

    def go_left_end(self):
        self.move_left = False

    def go_right_start(self):
        self.move_right = True

    def go_right_end(self):
        self.move_right = False

    # def go_right_end(self):
    #     new_x = self.xcor() + 20
    #     self.goto(new_x, self.ycor())


