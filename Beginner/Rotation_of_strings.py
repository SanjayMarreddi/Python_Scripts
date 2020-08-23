def rotation(a,n):
    "Rotate string 'a' by n times "
    c=[]
    for i in range(len(a)):
        b=chr(ord(a[i])+n)
        c.append(b)
    
    z='*'
    d=z.join(c)
    print (str(d))

    
rotation("cheer",1)      
