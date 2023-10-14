from turtle import Turtle

class Tile(Turtle):

    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.right(90)
        self.shapesize(stretch_wid=9.8, stretch_len=1)
        # self.fillcolor("blue")
        self.penup()
        self.goto(position)
