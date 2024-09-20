from turtle import Turtle, Screen

Screen().setup(500,500)
turtle = Turtle()

def draw_polygon(sides: int, sideLength: int = 50):
    for i in range(sides):
        turtle.forward(sideLength)
        turtle.left(360/sides)
        Screen().update()

draw_polygon(int(input('Number of sides ?')))

Screen().exitonclick()