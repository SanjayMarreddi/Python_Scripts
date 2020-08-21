N=raw_input().split()
a=[]
for i in N:
	a.append(i)

class polynomial:
	numpol=0
	def __init__(self,a):
		self.list1=a
		polynomial.numpol=self.numpol+1   # No of times the polynomial is called.
	def getReturn(self):
		return "Degree of the polynomial",(len(self.list1)-1)

	def getCoefficient(self,e):
		for i in range(len(self.list1)):
			if i==e:
				return "coefficient of the term",self.list1[i]

	def getFunction(self):
		self.sum="" #Creates an empty string.   # Using str() has advantage of taking variables and then it converts into STRING.
		for k in range(len(self.list1)):
			if int(self.list1[len(self.list1)-1-k]) != 0:
				self.sum=self.sum+ "+"+str( self.list1[len(self.list1)-1-k])+"X^"+str(len(self.list1)-1-k)
			
		return self.sum

	def evaluate(self,x):
		self.sum=0
		for k in range(len(self.list1)):
			if int(self.list1[len(self.list1)-1-k]) != 0:
				self.sum=self.sum+ (int(self.list1[len(self.list1)-1-k]))*(x**(int(len(self.list1)-1-k)))
			
		return "Function evaluated is",self.sum
	
		
p1=polynomial(a)  #Actually the class name itself is not taking any arguments ,But still the constructor takes 1 argument .
		  # It calls the constructor "__init__" 		  
print p1.getReturn()
print p1.getCoefficient(2) 
poly1=p1.getFunction()
print poly1
print p1.evaluate(4)

N=raw_input().split()
b=[]
for i in N:
	b.append(i)
c=zip(a,b)
f=[]
for i in c:
	d=int(i[0])+int(i[1])
	f.append(d)
p2=polynomial(f)
poly2=p2.getFunction()
print poly2
print polynomial.numpol
