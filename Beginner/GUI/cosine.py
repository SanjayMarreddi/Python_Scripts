import turtle
import math
SC=turtle.Screen()
SC.bgcolor("Pink")
S=turtle.Turtle()
SC.setworldcoordinates(-415,-400,415,400)
S.forward(815)
S.stamp()
S.backward(815)
S.left(90)
S.forward(800)
S.home()
S.right(90)
S.forward(815)
S.home()

S.backward(800)
S.stamp()
S.penup()

san=turtle.Turtle()
san.pencolor("Green")
i=-360
while i < 720:
	if i==-360:
		san.penup()
		san.goto(i,(math.cos(i*(math.pi/180))*250))
	
	else:
		san.pendown()
		san.goto(i,(math.cos(i*(math.pi/180))*250))

	i=i+1

SC.exitonclick()
