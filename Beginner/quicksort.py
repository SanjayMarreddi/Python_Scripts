def quicksort(L):
    if L==[]:
        return []
    else:
        return quicksort (filter(lambda x:x<L[0],L))  +[L[0]] + quicksort (filter(lambda x:x>L[0],L ))

M=[1,24,2,1,21]
                
print quicksort(M)
   
