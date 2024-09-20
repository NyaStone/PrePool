import turtle
toto = turtle . Screen () #retrieve the screen singleton object to manipulate the window
toto . bgcolor ("black") #change the background to black
titi = turtle . Turtle () # create a new turtle instance
titi . color ("red") # change it's color to red
for i in range (3) : # loop 3 times
    titi . right (90) # turn the turtle 90° in a anti-clocwise direction
    titi . circle (42) # make the turtle draw a circle with 42 pixel radius, those cirles will overlap
    toto . exitonclick () # pauses the execution until the window is clicked

# once the loop is done, the window will close