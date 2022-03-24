"""
w = forwards
s = backwards
a = counter-clockwise
d = clockwise
l = left
r = right
c = clear the screen
"""

from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def move_forwards():
    timmy.forward(10)

def move_backwards():
    timmy.back(10)

def counter_clockwise():
    timmy.circle(radius=20, extent=20, steps=10)

def clockwise():
    timmy.circle(radius=-20, extent=20, steps=10)

def turn_left():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)

def turn_right():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)

def clear():
    timmy.clear()

screen.listen()
screen.onkey(move_forwards, "w") # no () - function passed as input
screen.onkey(move_backwards, "s")
screen.onkey(counter_clockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(turn_left, "l")
screen.onkey(turn_right, "r")
screen.onkey(clear, "c")
screen.exitonclick()