k=input("Enter the months:-")
cur=1
prev=0
gen=2
if k==0:
	print("The total pairs are zero")
	exit
elif k==1 or 2:
	print("The total pairs are one ")
	exit
else:
	while gen<=k:
		new=cur+prev
		prev=cur
		cur=new
		gen=gen+1
	print("The total paris are",new)
	
	
	
