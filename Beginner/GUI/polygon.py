import math
import turtle
bob=turtle.Turtle()
def polygon(bob,length,sides):
    for i in range(int(sides)):
        bob.fd(length)
        bob.lt(360/sides)
sanjay=turtle.Turtle()

def circle(bob,r):
    cir=2*math.pi*r
    n=int(cir/3)+3
    length=cir/n
    polygon(bob,length,n)

circle(sanjay,20)























turtle.mainloop()
