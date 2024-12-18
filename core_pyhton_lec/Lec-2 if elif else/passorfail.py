#WAP to accept percentage from user and make a decision about his grade.
#if percentage greater than 70 mark as O grade otherewise if greater than 60 
#mark as A Grade and if it is more than 40 then B grade otherwise failed.


Marks=int (input("Enter Your Marks: "))
if Marks>100:
    print("Invalid Marks")
elif Marks>=70:
    print("You've got an O Grade CONGRATULATIONS!!")
elif Marks>=60:
    print("You've got an A Grade CONGRATULATIONS!!")
elif Marks>=40:
    print("You've got an B Grade CONGRATULATIONS!!")

else:
    print("You've failed")
       
