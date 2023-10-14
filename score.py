import turtle

class Score(Turtle):

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