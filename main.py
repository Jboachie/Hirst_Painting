# import colorgram
# rgb_colours = []
# hirst = colorgram.extract("image.jpg",30)
# for colour in hirst:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     new_color = (r, g, b)
#     rgb_colours.append(new_color)
#
# print(rgb_colours)

from turtle import Turtle, Screen
import random
screen = Screen()
screen.colormode(255)

joe = Turtle()
colors = [(206, 159, 83), (56, 89, 129), (144, 92, 41), (221, 206, 108), (139, 27, 49), (133, 175, 201), (156, 48, 83), (45, 55, 103), (168, 160, 41), (130, 188, 144), (83, 21, 44), (38, 43, 66), (185, 94, 107), (186, 140, 167), (86, 119, 178), (58, 39, 32), (79, 153, 164), (89, 156, 92), (194, 80, 73), (45, 74, 77), (162, 202, 218), (79, 74, 44), (57, 126, 124), (218, 176, 187), (221, 181, 168), (169, 206, 171)]
y_pos = -150
y_pos_final = y_pos + (10*50)

joe.teleport(-150,-150)
def draw_dots():
    for x in range(10):
        joe.color(random.choice(colors))
        joe.dot(20)
        joe.penup()
        joe.forward(50)
        joe.pendown()
while y_pos < y_pos_final:
    draw_dots()
    y_pos += 50
    joe.teleport(-150,y_pos)

























screen.exitonclick()