costs=0
units=int (input("Enter Number of Units: "))
if units>0 and units<=100 :
    costs=units*10
elif units>100 and units<=200 :
    costs=100*10+(units-100)*15
elif units>200 and units<=300 :
    costs=100*10+100*15+(units-200)*20
elif units>300 :
    costs=100*10+100*15+100*20+(units-300)*25
else:
    print("Please enter a valid input!!")

print(f"The Amount to be Paid will be: ₹{costs}")
