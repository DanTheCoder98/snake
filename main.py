import turtle
import time
import snake
import food
import scoreboard

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My Snake Game")

segments = snake.Snake()
items = food.Food()
score_board = scoreboard.ScoreBoard()

screen.listen()
screen.onkey(segments.up, "Up")
screen.onkey(segments.down, "Down")
screen.onkey(segments.left, "Left")
screen.onkey(segments.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    segments.move()

    if segments.head.distance(items) < 15:
        items.refresh()
        segments.extend()
        score_board.increase_score()

    if (
        segments.head.xcor() > 280
        or segments.head.xcor() < -280
        or segments.head.ycor() > 280
        or segments.head.ycor() < -280
    ):
        score_board.reset()

    for seg in segments.segments[1:]:
        if segments.head.distance(seg) < 10:
            score_board.reset()

screen.exitonclick()
