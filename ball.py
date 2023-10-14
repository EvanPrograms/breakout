from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        # self.fillcolor("orange")
        self.penup()
        self.goto(0, -200)
        self.x_move = 1
        self.y_move = 1
        # self.move_speed = 100

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_paddle(self, value):
        movement = value * 0.01
        self.y_move *= -1
        self.x_move = movement
        # self.move_speed *= 1.1



    # def bounce_paddle(self, value):
    #     movement = value * 0.02
    #     self.y_move *= -1
    #     if self.x_move >= 0:
    #         old_speed = self.x_move
    #         new_speed = movement * old_speed
    #         if abs(new_speed) > 2:
    #             self.x_move = 2
    #             print(self.x_move)
    #         else:
    #             self.x_move = new_speed
    #             print(self.x_move)
    #     if self.x_move < 0:
    #         old_speed_test = self.x_move
    #         new_speed_test = -movement * old_speed_test
    #         if abs(new_speed_test) > 2:
    #             if -movement >= 0:
    #                 self.x_move = -2
    #                 print(self.x_move)
    #             else:
    #                 self.x_move = 2
    #                 print(self.x_move)
    #         else:
    #             self.x_move = new_speed_test
    #             print(self.x_move)
    #         # self.x_move *= -movement
    #         # print(self.x_move)

    def bounce_x(self):
        self.x_move *= -1
        # self.move_speed *= 0.9

