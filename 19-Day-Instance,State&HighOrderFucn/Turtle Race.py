from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race, enter a colour")
colors = ["red","orange","magenta","black","green","blue","purple"]
all_turtles = []
is_race_on = False


for i in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100+(i*50))
    all_turtles.append(new_turtle)
    

if user_bet:
    is_race_on = True

while is_race_on:
    
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print("Hurray!turtle of color {} is the winner".format(winner))
            else:
                print("you lost ! {} is the winner".format(winner))
            
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        
screen.exitonclick()
