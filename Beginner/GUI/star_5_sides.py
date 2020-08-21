import math
import turtle
sc=turtle.Screen()
t=turtle.Turtle()
s=input("Enter the length of star :-")
t.pencolor("Red")
for i in range(5):
    t.forward(s)
    t.right(144)

a=math.radians(18)
b=math.radians(144)

r=s*(math.sin(a)/math.sin(b))

t.right(108)
t.pencolor("Blue")
t.circle(r)
sc.exitonclick()
