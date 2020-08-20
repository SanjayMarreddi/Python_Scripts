# cook your dish here
import string

L=list(string.ascii_uppercase) 

n= 5
for i in range(1,n+1):
    for j in range(i):
        print(L[i-1], end=" ")
    
    print("\n")
    
    
    

    