# cook your dish here

def GCD(x,y):
    
    x = max(x,y)
    y = min(x,y)
    
    while (x and y) :
        
        n = x%y
        x = y
        y = n

    print (x)
    return (x)
    

def LCM(a,b):
    return ( (a*b)/GCD(a,b) )


print(LCM(96,72),LCM(120,33))