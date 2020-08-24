def printmatrix(M):
    for i in range(len(M)):
        print M[i]

def listmaker(n):
    a=[]
    for i in range(n):
        a.append(0)
    return a

def matrixmaker(m,n):           # m rows and n columns
    b=[]
    for j in range(m):
        b.append(listmaker(n))
    return b

printmatrix(matrixmaker(3,3))

def identitymatrix(n):
    c=matrixmaker(n,n)
    for i in range(n):
        c[i][i]=1
    return c

printmatrix(identitymatrix(3))


def addlists(A,B):
    C=listmaker(len(A))
    for i in range(len(A)):
        C[i]=A[i]+B[i]
    return C

def addmatrices(X,Y):
    D=listmaker(len(X))
    for i in range(len(X)):
        D[i]=addlists(X[i],Y[i])
    return D

printmatrix(addmatrices(identitymatrix(4),identitymatrix(4)))



