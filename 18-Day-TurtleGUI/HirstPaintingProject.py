import turtle as t
import colorgram
import random

tim = t.Turtle()
tim.speed("fastest")
tim.hideturtle()
tim.penup()

scr =t.Screen()
scr.colormode(255)


colors = colorgram.extract("images\Hirst.jpg", 30)
rgb_list = []

for clr in colors:
    rgb = clr.rgb
    r = rgb.r
    g = rgb.g
    b = rgb.b
    rgb_tuple = (r, g, b)
    rgb_list.append(rgb_tuple)

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
no_of_dots = 100

for dot_count in range(1, no_of_dots+1):
    tim.dot(20, random.choice(rgb_list))
    tim.forward(50)

    if dot_count % 10 ==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

scr.exitonclick()
