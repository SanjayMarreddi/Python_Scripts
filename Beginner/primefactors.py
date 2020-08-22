import math
def primeFactors(n):
    a=[]
    while n % 2 == 0: 
        a.append(2)
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i== 0: 
            a.append(i)
            n = n / i 
    if n > 2: 
        a.append(n)
    return a

print primeFactors(input())
import math
N=input()
num=[]
for i in range(N):
    x,y=raw_input().split()
    X=int(x)
    for i in range(int(y)):
        num.append(X)

print "Initial list", num
