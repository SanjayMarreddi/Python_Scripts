def flatten(lls):
  fl = []
  for ls in lls:
     fl.append(sum(ls))
  return fl

def tpose(lls):
    tls=[]
    tlen = 0
    for ls in lls:
        tlen = max(tlen, len(ls))
    for i in range(tlen):
        tls.append([])
    for ls in lls:
        for i in range(len(ls)):
            tls[i].append(ls[i])

    return tls

print flatten([[1,2,3],[0,1]])
tls=tpose([[1,2,3],[0,1]])
print tls

