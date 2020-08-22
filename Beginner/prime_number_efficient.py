import math
x=input("The Number to be verified:-")
i=2
while i<=(math.sqrt(x)):
	if x%i==0: 
		print("The given number is Not PRIME!!")
		break
	i=i+1
else:
	print("The given number is PRIME!")
