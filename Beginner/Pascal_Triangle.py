				#defining a function to calculate factorial
def factorial(n):
	a=1
	for i in range(1,n+1):
		a=a*i
	return a

def bincof(x,y):
	return factorial(x)/(factorial(y)*factorial(x-y))
def row(z):
	for i in range(z+1):
		print bincof(z,i),
	print ("\n")

for i in range (11):
	row(i)
