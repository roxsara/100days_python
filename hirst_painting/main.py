# Create an image similar to a Hirst painting: 10x10 dots of color
# Using the colorgram module to extract the most used colors from the image
# The list build manually is excluding the colors too close to white

# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)

import turtle as t
import random

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]

timmy = t.Turtle()
t.colormode(255)


def random_color():
    return random.choice(color_list)


timmy.hideturtle()
timmy.penup()
timmy.speed("fastest")
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

for column in range(10):
    for line in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.forward(50)
    if column % 2 == 0:
        timmy.back(50)
        timmy.left(90)
        timmy.forward(50)
        timmy.left(90)
    else:
        timmy.back(50)
        timmy.right(90)
        timmy.forward(50)
        timmy.right(90)

screen = t.Screen()
screen.exitonclick()