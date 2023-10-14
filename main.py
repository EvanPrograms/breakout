from tkinter import *
from turtle import Screen
import time
from paddle import Paddle
from tile import Tile
from ball import Ball
# from score import Score

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Breakout Game")

paddle_position = (0, -250)
paddle = Paddle(paddle_position)

x_values = [-400, -200, 0, 200, 400]
y_values = [250, 225, 200, 175, 150, 125, 100]
color = ["red", "orange", "yellow", "green", "blue", "purple", "teal"]
brick_list = []
for x in x_values:
    for y in y_values:
        color_choice = color[y_values.index(y)]
        tile_position = (x, y)
        tile = Tile(tile_position, color_choice)
        brick_list.append(tile)

# tile = Tile((0, 300), "red")
# brick_list.append(tile)

ball = Ball()

left_keys = ["a", "A", "Left"]
right_keys = ["d", "D", "Right"]

screen.listen()
for key in left_keys:
    screen.onkeypress(paddle.go_left_start, key)
    screen.onkeyrelease(paddle.go_left_end, key)
for key in right_keys:
    screen.onkeypress(paddle.go_right_start, key)
    screen.onkeyrelease(paddle.go_right_end, key)


# tile_set = 0
game_is_on = True

def collision(item_a, item_b):
    if item_b.ycor() - 20 <= item_a.ycor() <= item_b.ycor() + 20 and item_b.xcor() - 100 <= item_a.xcor() <= item_b.xcor() + 100:
        return True


frame = 0
tile_set = 0
def breakout():
    game_is_on = True
    global tile_set
    global brick_set
    global frame
    screen.update()
    brick_frame = 0
    paddle_frame = 0
    ball.move()
    if paddle.move_left:
        if paddle.xcor() - 100 > -500:
            x = paddle.xcor()
            x -= 2
            paddle.setx(x)
    if paddle.move_right:
        if paddle.xcor() + 100 < 500:
            x = paddle.xcor()
            x += 2
            paddle.setx(x)
    if ball.xcor() > 480 or ball.xcor() < -480:
        ball.bounce_x()
    for brick in brick_list:
        if collision(ball, brick):
            if frame - brick_frame > 1:
                brick_frame = frame
                brick.hideturtle()
                brick_list.remove(brick)
                ball.bounce_y()
                tile_set = 1
    if paddle.xcor() - 110 <= ball.xcor() <= paddle.xcor() + 110 and ball.ycor() == -230 and tile_set == 1:
        value = ball.xcor() - paddle.xcor()
        print(value)
        ball.bounce_paddle(value)
        tile_set = 0
    if ball.ycor() > 280:
        tile_set = 1
        ball.bounce_y()
    if ball.ycor() == -300:
        game_is_on = False
    if brick_list == []:
        print("you win!")
        return False
    frame += 1



while game_is_on:
    time.sleep(0.001)
    if breakout() is False:
        game_is_on = False
