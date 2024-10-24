import turtle
from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(500,400)
guess = screen.textinput("Make you bet","Which turtle will win the race? Enter the color: ")
colors = ["red","green","blue","orange","yellow","indigo"]
y = [-70,-40,-10,20,50,80]
is_race_on = False
all_turtle = []

for turtle_index in range(6):
    tim = Turtle("turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(-230,y[turtle_index])
    all_turtle.append(tim)

print(all_turtle)
if guess:
    is_race_on = True
while is_race_on:
    for i in all_turtle:
        if(i.xcor()>230):
            is_race_on = False
            winner = i.pencolor()
            if winner==guess:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")

        distance = random.randint(1,10)
        i.forward(distance)



screen.exitonclick()