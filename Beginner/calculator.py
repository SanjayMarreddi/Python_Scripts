from Tkinter import *
import math

O=[]

def dosqrt():
    num=float(entry.get())
    sqrtnum = math.sqrt(num)
    entry.delete(0,END)
    entry.insert(0,str(sqrtnum))

def factorial():
    num=float(entry.get())
    fac= math.factorial(num)
    entry.delete(0,END)
    entry.insert(0,str(fac))

def add():
	l=[]
	global O
	global l
	
	a=entry.get()
 	num1=float(a)
	n=len(a)
	global n
	entry.insert(n,"+")
	O.append("+")
	l.append(num1)	
	
def subtract():
	l=[]
	global l
	global O
	a=entry.get()
 	num1=float(a)
	n=len(a)
	global n
	entry.insert(n,"-")
	O.append("-")
	l.append(num1)	
def mul():
	l=[]
	global O
	global l
	a=entry.get()
 	num1=float(a)
	n=len(a)
	global n
	entry.insert(n,"*")
	O.append("*")
	l.append(num1)

def div():
	l=[]
	global O
	global l
	a=entry.get()
 	num1=float(a)
	n=len(a)
	global n
	entry.insert(n,"/")
	O.append("/")
	l.append(num1)	
def power():
	l=[]
	global O
	global l
	a=entry.get()
 	num1=float(a)
	n=len(a)
	global n
	entry.insert(n,"^")
	O.append("^")
	l.append(num1)	

def evaluate():
	global l
	global n
	global O
	entry.delete(0,n+1)
	res=entry.get()
	l.append(int(res))
	entry.delete(0,END)
	if O[0]=="+":
		z=str(sum(l))
		entry.insert(0,z)
	
	if O[0]=="-":
		z=str(l[0]-l[1])
		entry.insert(0,z)
	if O[0]=="*":
		z=str((l[0])*(l[1]))
		entry.insert(0,z)
	if O[0]=="/":
		z=str((l[0])/(l[1]))
		entry.insert(0,z)
	if O[0]=="^":
		z=str((l[0])**(l[1]))
		entry.insert(0,z)
		
	l=[]
	O=[]


def func(i):
	n=len(entry.get())	
	entry.insert(n,i)

root = Tk()
entry = Entry(root)

name=Label(root,text="My Calculator")

zb = Button(root, text="0", command= lambda: func(0))
ob = Button(root, text="1", command= lambda: func(1))
tb = Button(root, text="2", command= lambda: func(2))
ttb = Button(root, text="3", command= lambda: func(3))
fb = Button(root, text="4", command= lambda: func(4))
ffb = Button(root, text="5", command= lambda: func(5))
sb = Button(root, text="6", command= lambda: func(6))
ssb = Button(root, text="7", command= lambda: func(7))
eb = Button(root, text="8", command= lambda: func(8))
nb = Button(root, text="9", command= lambda: func(9))

sqrtb = Button(root, text="Sqrt", command=dosqrt)
addb = Button(root, text="+", command=add)
subtb = Button(root, text="-", command=subtract)
mulb = Button(root, text="*", command=mul)
divb = Button(root, text="/", command=div)
powb = Button(root, text="^", command=power)
factorialb=Button(root, text="!", command=factorial)
equalb=Button(root, text="=", command=evaluate)
exitb = Button(root, text="Exit", command=quit)

name.grid(row=0,column=0,columnspan=5)

entry.grid(row=1,column=0,columnspan=5)

ob.grid(row=2,column=0)
tb.grid(row=2,column=1)
ttb.grid(row=2,column=2)

fb.grid(row=3,column=0)
ffb.grid(row=3,column=1)
sb.grid(row=3,column=2)

ssb.grid(row=4,column=0)
eb.grid(row=4,column=1)
nb.grid(row=4,column=2)

zb.grid(row=5,column=0)
sqrtb.grid(row=5,column=1)
powb.grid(row=5,column=2)

addb.grid(row=2,column=3)
subtb.grid(row=3,column=3)
mulb.grid(row=4,column=3)
divb.grid(row=5,column=3)
factorialb.grid(row=6,column=0)
equalb.grid(row=6,column=1)
exitb.grid(row=6,column=2)
root.mainloop()

