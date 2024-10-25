import turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

snake_segments = []

start_x = 0

for turtles in range(3):
    new_turtle = turtle.Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.goto(start_x, 0)

    start_x -= 20
    snake_segments.append(new_turtle)

screen.exitonclick()