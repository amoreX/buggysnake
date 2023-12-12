import turtle
from snake import Snake 
import time
screen=turtle.Screen()
screen.setup(width=900,height=700)
screen.bgcolor("black")
screen.title("Snakey Game <3")
screen.tracer(0)
turtle.listen()

snake=Snake()

screen.update()

screen.listen()
screen.onkey(snake.move_left,"Left")
screen.onkey(snake.move_right,"Right")
screen.onkey(snake.move_up,"Up")
screen.onkey(snake.move_down,"Down")


while True:
    snake.move()
    screen.update()
    time.sleep(0.1)    
    

turtle.exitonclick()