# cook your dish here

def Arm(a,b):
    
    for i in range(a,b+1):
        s= str(i)
        x =int(s[0])
        y =int(s[1])
        z =int(s[2])
        if (x**3)+ (y**3)+ (z**3) == i :
            print(i)
            
            
            
Arm(100,999)