# cook your dish here

from math import factorial
 
n=6
x=3

c=2
s=0

for i in range(0,n+1,2):
    
    s +=( ( (-1)**c  ) * (  (x**i)/(factorial(i))    ))
    c +=1

print(s)
