known={0:0,1:1}
def fibonnaci(n):
    if n in known:
        return known[n]
    else:
        b=fibonnaci(n-1)+fibonnaci(n-2)
        known[n]=b
        return b

print fibonnaci(input())  
