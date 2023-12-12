import turtle
import random
segments=list()
screen=turtle.Screen()
start_position=[(0,0),(-20,0),(-40,0)]
text_turtle=turtle.Turtle()
text_turtle.hideturtle()
score=0
message="Your score is:"+str(score)
def update_score(msg):
        text_turtle.clear() 
        text_turtle.penup()
        text_turtle.goto(0, screen.window_height() // 2 - 30)  
        text_turtle.color("white")
        text_turtle.write(msg, align="center", font=("Arial", 16, "normal"))
class Snake:
    def __init__(self):
        self.segments=list()
        self.segment_width=20
        self.create_snake()
        self.create_food()
        update_score(message)
        self.head=self.segments[0]
    
    def create_snake(self):
        for pos in start_position:
            new_sq=turtle.Turtle("square")
            new_sq.color("white")
            new_sq.penup()
            new_sq.width(self.segment_width)
            new_sq.goto(pos)
            self.segments.append(new_sq)
    
    def create_food(self):
        self.food=turtle.Turtle("square")
        self.food.color("red")
        self.food.penup()
        self.food.shapesize(stretch_wid=0.35, stretch_len=0.35, outline=0)
        self.food.goto(int(random.randint(-290,290)),int(random.randint(-290,290)))
    
    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            self.segments[i].goto(self.segments[i-1].pos())
        self.head.forward(20)
        for i in range(len(self.segments)-1,0,-1):
            if self.head.distance(self.segments[i])<10:
                turtle.bye()
                print("Game Over")
        if self.head.distance(self.food)<15:
            global score
            score+=1
            message="Your score is:"+str(score)
            update_score(message)
            self.food.goto(int(random.randint(-290,290)),int(random.randint(-290,290)))
            self.segment_width+=4
            self.create_snake()
            
            
    def move_up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)
        
    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
        
    def move_left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)
        
    def move_right(self):
        if self.head.heading()!=180:
            self.head.setheading(0)
    