from turtle import *

speed(100000000000000)
width(3)

#drawning house

#background
bgcolor("green")
goto(0,-200)
color("cyan")
begin_fill()
forward(951)
left(90)
forward(950)
left(90)
forward(1910)
left(90)
forward(950)
end_fill()

#house square
left(90)
forward(700)
color("orange")
begin_fill()
left(90)
forward(250)
right(90)
forward(200)
right(90)
forward(250)
end_fill()

#attic
color("red")
penup()
right(180)
forward(250)
pendown()
begin_fill()
left(30)
forward(200)
left(119)
forward(200)
end_fill()
penup()
left(31)
forward(250)

#door
begin_fill()
left(90)
forward(70)
pendown()
left(90)
forward(120)
right(90)
forward(70)
right(90)
forward(120)
end_fill()
left(90)
penup()
forward(63)
left(90)

#window
color("blue")
forward(160)
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

penup()
goto(-260,-200)
left(90)
forward(162)
right(90)
forward(20)
pendown()
begin_fill()
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()













exitonclick()