def most_frequent(string):
    d=dict()
    count=0
    for x in string:
            if x not in d:
                d[x]=1
            else:
                d[x]=d[x]+1

    a=[]        
    for x in d:
        y=d[x]
        a.append(y)

    a.sort()
    b=a[::-1]
    print b
    count=0
    for i in b:
        for k in d:
            if d[k]==i:
                print k
                count=count+1
            if count>len(b)-1:
                break

string="saannnjjjjyyyyy"
most_frequent(string)
