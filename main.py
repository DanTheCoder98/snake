import turtle
import time
import snake

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My Snake Game")

segments = snake.Snake()

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

screen.exitonclick()