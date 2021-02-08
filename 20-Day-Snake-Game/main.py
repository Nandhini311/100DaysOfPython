from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("MY Snake Game")
screen.tracer(0) #untill we call update, the screen won't show what we have done

snake = Snake()

screen.listen
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    

screen.exitonclick()
