
# If difference between Consecutive Primes is 2 They are called TWIN PRIMES

import math

def prime(n): 
    i=2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i+=1
    
    return True


primes=[]
for e in range(2,100):
    if prime(e):
        primes.append(e)


twin=[]

for j in range(len(primes)-1):
    if (primes[j+1]- primes[j] == 2) :
        twin.append([primes[j],primes[j+1]])

print(twin)