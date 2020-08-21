from Tkinter import *
import tkFont
import math
flag=False
count=99

def dostart():
    global flag
    global count
    flag=True
    def countdown():
        global flag
        global count
        if flag==True:
            count=count-1
            head["text"]=str(count)
            head.after(1000,countdown)
    countdown()

def dostop():
    global flag
    flag=False

def doreset():
    global count
    count = 99


root = Tk()

font=tkFont.Font(size="32")


 
head= Button(root,text=str(count),font=font)
startb = Button(root, text="Start", command=dostart)
stopb = Button(root, text="Stop", command=dostop)
resetb = Button(root, text="Reset", command=doreset)

head.grid(columnspan=2)
startb.grid(row=1,column=0)
stopb.grid(row=1,column=1)

resetb.grid(columnspan=2)

root.mainloop()

