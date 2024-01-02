import random
import turtle as t
from turtle import Screen
import colorgram

# Making a random walk using random color

tim = t.Turtle()
t.colormode(255)

def random_color():
    r= random.randint(0,255)
    g = random.randint ( 0, 255 )
    b = random.randint ( 0, 255 )
    return (r, g, b)

random_num = [0,1, 2]
for num in range(200):
    tim.pendown()
    tim.speed(0)
    tim.pensize(10)
    tim.color(random_color())
    if random.choice(random_num) == 0:
        tim.right ( 90 )

    elif random.choice(random_num) == 1:
        tim.back(30)
    else:
        tim.forward ( 30 )

    tim.left(90)




