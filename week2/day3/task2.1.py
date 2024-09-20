from turtle import Turtle, Screen
import time

Screen().setup(500, 500)
turtle = Turtle(visible=False)

for i in range(4):
    turtle.forward(100)
    turtle.left(90)
    Screen().update()

Screen().exitonclick()