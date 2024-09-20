from turtle import Turtle, Screen

Screen().setup(500, 500)

turtle = Turtle()

# draw a sequence of parts of circles that have an increasing radius
for i in range(0, 500, 2):
    turtle.circle(i, 30) 

Screen().update()
Screen().exitonclick()
