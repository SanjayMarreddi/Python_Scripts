def most_frequent(string):
    a=[]
    for i in range(len(string)):
        count=0
        for x in string:
            if string[i]==x:
                count=count+1
                a.append(count)
    print a

string="sanjay"
most_frequent(string)
