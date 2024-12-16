#თქვენი სიტყვებით ახსენით რა არის ცვლადი, ცვლადის სახელი, ცვლადის მნიშვნელობა. ასევე ახსენით რაში გვადგება ცვლადები

#




#პითონის turtle ბიბლიოთეკის გამოყენებით შექმენით ძალიან დიდი სასახლე

from turtle import *

shape ("arrow")
width (8)
speed(400)

#drawning square 

color ("dimgrey")

begin_fill()
forward (450)
right(90)
forward(450)
right(90)
forward (700)
right(90)
forward(450)
right(90)
forward(700)

end_fill()


#drawning 2 large squares 

#first large square


penup()
forward (120)
pendown()

color("gray")
begin_fill()

right(90)
forward(450)
right(90)
forward(120)
right(90)
forward(750)
right(90)
forward(120)
left(90)
forward(50)
left(90)
forward(30)
left(90)
forward(50)
right(90)
forward(15)
right(90)
forward(50)
left(90)
forward(30)
left(90)
forward(50)
right(90)
forward(15)
right(90)
forward(50)
left(90)
forward(30)
left(90)
forward(50)

left(90)
forward(120)
right(90)
forward(750)


end_fill()

#second large square

penup()
goto(0,0)
right(90)
forward(250)
pendown()


begin_fill()

left(90)
forward(450)
right(90)
forward(120)
right(90)
forward(745)
right(90)
forward(120)
left(90)
forward(50)
left(90)
forward(30)
left(90)
forward(50)
right(90)
forward(15)
right(90)
forward(50)
left(90)
forward(30)
left(90)
forward(50)
right(90)
forward(15)
right(90)
forward(50)
left(90)
forward(30)
left(90)
forward(50)

left(90)
forward(120)
right(90)
forward(300)

end_fill()

#drawning a gate


penup()
forward(450)
left(90)
forward(250)
pendown()


color("chocolate4")
begin_fill()
left(90)
forward(250)
right(90)
forward(200)
right(90)
forward(250)

end_fill()


right (180)
forward(110)
penup()
left(90)
forward(80)
pendown()


#drawning a gate handles

color("black")

width(5)

begin_fill()
right(90)
forward(15)
left(90)
forward(15)
left(90)
forward(20)
left(90)
forward(15)
end_fill()

right(180)
forward(15)
 
penup()
forward(15)
pendown()

begin_fill()
right(90)
forward(20)
left(90)
forward(15)
left(90)
forward(20)
left(90)
forward(15)
end_fill()

#drawing windows



width(12)

color("chocolate3")

penup()
goto (0,0)
forward(450)
left(90)
forward(120)
right(90)
penup()
forward(40)
left(90)
pendown()

begin_fill()

forward(75)
right(90)
forward(40)
right(90)
forward(75)
right(90)
forward(40)

end_fill()


penup()
goto(0,0)

forward(250)
right(90)
forward(120)
left(90)
forward(40)
begin_fill()

right(90)
pendown()
forward(75)
left(90)
forward(40)
left(90)
forward(75)
left(90)
forward(40)
end_fill()

width(9)

color("chocolate3")

penup()
goto(0,0)
right(180)

forward(250)

right(180)
forward(100)
right(90)
forward(180)
pendown()

begin_fill()

left(90)
forward(60)
left(90)
forward(80)
left(90)
forward(60)
left(90)
forward(80)

end_fill()



penup()
goto(450,0)
right(90)
forward(100)
left(90)
forward(180)
right(90)
pendown()

begin_fill()

forward(60)
right(90)
forward(80)
right(90)
forward(60)
right(90)
forward(80)

end_fill()



#End of drawning windows

color("grey")

width(5)

penup()
goto(450,0)
right(90)
forward(50)
pendown()

begin_fill()

right(90)
forward(60)
left(90)
forward(40)
left(90)
forward(60)
end_fill()

right(90)


penup()
forward(50)
pendown()

begin_fill()
right(90)
forward(60)
left(90)
forward(40)
left(90)
forward(60)
end_fill()

penup()
right(90)
forward(50)
pendown()

begin_fill()

right(90)
forward(60)
left(90)
forward(40)
left(90)
forward(60)

end_fill()

penup()
right(90)
forward(50)
pendown()

begin_fill()

right(90)
forward(60)
left(90)
forward(40)
left(90)
forward(60)

end_fill()

penup()
right(90)
forward(50)
pendown()

begin_fill()

right(90)
forward(60)
left(90)
forward(40)
left(90)
forward(60)

end_fill()

penup()
right(90)
forward(50)
pendown()

begin_fill()
right(90)
forward(60)
left(90)
forward(40)
left(90)
forward(60)
right(90)

end_fill()

penup()
forward(50)
right(90)
pendown()


begin_fill()
forward(60)
left(90)
forward(40)
left(90)
forward(60)
end_fill()






























exitonclick()