from turtle import Turtle, Screen
import random

tim = Turtle()
scr = Screen()

scr.colormode(255)

def random_rgb_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255) 
    return(r, g, b)

tim.speed('fastest')

# for pos in range(10):     
#     current_x_cor = tim.xcor() + pos
#     tim.setheading(current_x_cor)
#     tim.color(random_rgb_color())
#     tim.circle(100)

for pos in range(100):     
    current_heading = tim.heading()
    tim.setheading(current_heading + 5)
    tim.color(random_rgb_color())
    tim.circle(100)





scr.exitonclick()