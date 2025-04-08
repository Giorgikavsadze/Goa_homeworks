from turtle import *

shape("arrow")

speed(10)

width(4)

#DRAW A HOUSE 

#step 1 draw a square 


color("purple")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)

#step 2 draw a door 


left(90)
forward(75)
color("yellow")
begin_fill()
left(90)
forward(100)
right(90)
forward(50)
right(90)
forward(100)
end_fill()

#step 3 draw a roof 


penup()
goto(200, 200 )
pendown()

color("blue")
begin_fill()
right(150)
forward(180)
left(115)
forward(190)
end_fill()

#step 4 draw windows


color("purple")
goto(0,0)
right(145)
forward(120)
penup()
right(90)
forward(20)
left(90)
pendown()

color("green")
begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

penup()
goto(200,0)
right(90)
forward(120)
left(90)
forward(20)
right(90)

pendown()
begin_fill()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()
      


exitonclick()