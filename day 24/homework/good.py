# Boss level:
#good way

from turtle import *

def squares(x,y):


    penup()
    goto(x,y)
    pendown()
    speed(50)

    for i in range(4):
        forward(200)
        left(90)

squares(100,100)
squares(-300,100)
squares(-300,-300)
squares(100,-300)

exitonclick()