# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
c=input()
a=input()
b=math.sqrt((a)**2 +(c)**2)
x=b/2
z=x/a
res=math.degrees(math.asin(z))
R=math.trunc(res)
print ( str(R)+u'\u00b0')
