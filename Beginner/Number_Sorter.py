def sorter(x,y,z):
	if x>y and x>z:
		print("Maximum:-",x)
	if y>z and y>x:
		print("Maximum:-",y)
	if z>y and z>x:
		print("Maximum:-",z)
	if x<y and x<z:
		print("Minimum:-",x)
	if y<z and y<x:
		print("Minimum:-",y)
	if z<y and z<x:
		print("Minimum:-",z)
	if x>y>z or z>y>x:
		print("Middle:-",y)
	if y>x>z or z>x>y:
		print("Middle:-",x)
	if x>z>y or y>z>x:
		print("Middle:-",z)

x=input("Enter the first number:-")
y=input("Enter the second number:-")
z=input("Enter the third number:-")

sorter(x,y,z)

