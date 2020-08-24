def pattern1(n):
	a=["A ","B ","C ","D ","E ","F ","G ","H ","I ","J ","K ","L ","M ","N ","O ","P ","Q ","R ","S ","T ","U ","V ","W ","X ","Y ","Z "]
	for i in range(1,n+1):
		print (a[i-1]*i)
		print("")
n=int(input("Enter the number of rows:-"))
pattern1(n)


def pattern2(n):
	for i in range(1,n+1):		# n stands for the number of rows
		a=1   					# Every time the values start printing from one only#
		for j in range(i):		# This is the most crucial line which decides number of items to be print in a row
			print(a, end=" ")		
			a=a+1		
		print("\n")	

n=int(input("Enter the number of rows:-"))
pattern2(n)


def pattern3(n): 
      
    a= 1 
    for i in range(0, n): 
        for j in range(0, i+1): 
            print(a, end=" ")
            a=a+ 1
        print("\n")

n=int(input("Enter the number of rows:-"))
pattern3(n) 
  

