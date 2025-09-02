import turtle as t
import random

tim = t.Turtle()
scr = t.Screen()
tim.shape("turtle")
tim.color("green")
t.colormode(255)

turnAngle = [0,45,90,135,180,225,270]

for run in range(200):  
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255) 
    tim.color(r,g,b)
    tim.pensize(15) 
    # tim.setheading(random.choice(turnAngle))
    tim.setheading(random.randint(1,360))
    tim.forward(30)


scr.exitonclick()