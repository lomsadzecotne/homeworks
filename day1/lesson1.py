from turtle import *
speed(15)
width(7)
color("purple")

for i in range(4):
    forward(200)
    left(90)

#saxlis formis dasasruli

forward(70)
color("yellow")
begin_fill()
left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
end_fill()
#karebis dasasruli
penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#saxuravis dasasruli

penup()
goto(30,120)
pendown()

begin_fill()

color("brown")  #tu ginda lurji ravici aba me
left(120)

for i in range(4):
    forward(30)
    left(90)

end_fill()
# erti fanjara amovsebuli
penup()
forward(120)
pendown()

begin_fill()
for i in range(4):
    forward(30)
    left(90)
end_fill()

exitonclick()