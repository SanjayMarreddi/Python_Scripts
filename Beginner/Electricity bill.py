u=int(input("Enter the units consumed:-"))
bill=0
if u>400:
    bill=bill+(u-400)*8+100
    u=400
if u>200:
    bill=bill+(u-200)*5+50
    u=200
if u>100:
    bill=bill+(u-100)*3
    u=100
if u<100:
    print("Electricty bill charges:-40")
else :
    print("Electricity bill charges:-",bill)
    
