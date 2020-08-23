def sqrt(a):
    x=1
    while True:
        y=(x+a/x)/2.0
        if y==x:
            print (y)
            break
        else:
            x=y

sqrt(int(input("Enter the number:-")))
