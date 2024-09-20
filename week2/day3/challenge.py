from turtle import Turtle, Screen
import asyncio

Screen().setup(500,500)
Screen().update()
loop = asyncio.get_event_loop()

async def fractal_triangle(x: int, y: int, size: int):
    middlePoints: list[tuple[int, int]] = []
    turtle = Turtle()
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for i in range(3):
        turtle.forward(size/2)
        middlePoints.append(turtle.position())
        turtle.forward(size/2)
        turtle.right(360/3)
    turtle.hideturtle()
    if (size > 10):
        await asyncio.gather(
            fractal_triangle(turtle.position()[0], turtle.position()[1], size/2),
            fractal_triangle(middlePoints[0][0], middlePoints[0][1], size/2),
            fractal_triangle(middlePoints[2][0], middlePoints[2][1], size/2)
        )


loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(fractal_triangle(20, 20, 200))
    loop.run_until_complete(loop.shutdown_asyncgens())
finally:
    loop.close()
Screen().exitonclick()
