

a=[2,2,2,2,3,3,4,4,4,5,5,6,6,7,7,44,3,3,4,4,4,44,4465675678,78,558,558,55,678,8797890]

"""Bubble sort"""

i=0
while i<len(a)-1:
	j=0
	while j<len(a)-1-i:
		if a[j]>a[j+1]:
			x=a[j]
			a[j]=a[j+1]
			a[j+1]=x
		j=j+1
	i=i+1
print a

#Finding the frequency using the Binary search
x=input("Enter the number to be searched:-")
count=0
start=0
end=len(a)-1
while start<=end:
	mid=(start+end)/2
	if a[mid]==x:
		while start<=end:
			if a[end]==x:
				count=count+1
			end=end-1
	elif a[mid]>x:
		end=mid-1
	elif a[mid]<x:
		start=mid+1
	else:
		print(x,"not found")

print(x,"has appeared",count,"times")
