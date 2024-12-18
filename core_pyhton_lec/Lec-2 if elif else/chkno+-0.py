#WAP to check whether the number is zero, positive or negative
#to validate multiple conditions we need to use (if...elif...else)condition

a=int (input("Enter a number: "))
if a>0:
    print("Entered number is a positive number")
elif a<0:
    print("Entered number is a negative number")
else :
    print("The number is zero")
