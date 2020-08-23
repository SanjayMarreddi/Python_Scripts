# Selection
for j in range(len(a)-1):
    for i in range(j+1,len(a)):
        if a[j]>a[i]:
            a[i],a[j] =a[j],a[i]
            # Swap




# Bubble 
for j in range(len(a)-1):
    for i in range(len(a)-1-j):
        if a[i] > a[i+1]:
            a[i],a[i+1] =a[i+1],a[i]
            #Swap