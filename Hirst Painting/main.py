# from colorgram import extract
# rgb_colors = []
# colors = extract('art.jpeg',50)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r,b,g))
from turtle import Screen,Turtle
import random
import turtle
turtle.colormode(255)
tim = Turtle()
colors = [(183, 135, 160), (123, 78, 95), (147, 155, 171), (145, 175, 163), (181, 158, 148), (125, 92, 81), (43, 25, 34), (214, 149, 200), (79, 121, 105), (84, 96, 112), (45, 36, 27), (29, 45, 35), (25, 29, 37), (144, 92, 139), (163, 118, 106), (219, 171, 180), (216, 186, 177), (169, 98, 110), (175, 183, 203), (105, 118, 143), (110, 56, 40), (184, 206, 189), (103, 41, 47), (95, 150, 141), (114, 150, 122), (170, 206, 201), (72, 44, 71), (47, 63, 75), (53, 84, 60), (33, 87, 78)]
tim.setheading(225)
tim.speed("fastest")
tim.hideturtle()
tim.penup()
tim.forward(325)
tim.setheading(0)
no_of_dots = 100

for dot_count in range(1,no_of_dots+1):
    tim.dot(20,random.choice(colors))
    tim.forward(50)
    if dot_count%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)












screen = Screen()
screen.exitonclick()