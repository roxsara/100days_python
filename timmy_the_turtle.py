import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


timmy.shape("turtle")
timmy.color("pink")
timmy.pencolor("red")
timmy.speed("fastest")

"""
3 drawing a dashed line
for _ in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()
"""

"""
# drawing different shapes
for sides in range(3, 11):
    for side in range(sides):
        timmy.forward(100)
        timmy.right(360/sides)
"""

"""
# random walk
directions = [0, 90, 180, 270]
timmy.pensize(10)

for _ in range(200):
    timmy.pencolor(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))
"""


# drawing a spirograph
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + 10)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()