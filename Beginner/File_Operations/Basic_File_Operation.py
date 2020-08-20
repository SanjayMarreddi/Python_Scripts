L=[]
with open ("input.txt") as f:
    a= f.readlines()
    for i in a:
        i = i.rstrip() # Use strip method for removing "\n" line characters
        l= i.split("\t")
        L.append(l[::-1])
        

L.sort(reverse=True)
print(L)
for i in range(len(L)):
    L[i] = L[i][::-1]

print(L)

with open("output.txt","w") as o:
    for line in L:
        o.write(line[0]+ "\t" + line[1]+ "\t" + line[2] + "\t"+line[3]+ "\n")

    


