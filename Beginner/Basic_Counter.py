def Counter(s):
    d=dict()
    for i in s:
        if i not in d:
            d[i]=1
        else:
            d[i]=d[i]+1

    return d

b="Sanjay"
h=Counter(b)

for i in sorted(h):
    print( i,h[i])
