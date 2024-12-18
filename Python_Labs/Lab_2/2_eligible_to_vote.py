#WAP to check whether a person is eligible to vote or not.

#Enter your age
age=int (input("Enter Your Age: "))



#Checking Eligibility Criteria
#Age should be betwee 18 to 100 Eligible
if (age>=18) and (age<=100):    
    print("Yes your are eligible to Vote")


#Age is between 0 to 18 Not Eligible
elif (age>0) and (age<18):         
    years=18-age
    print(f"Your are not elgible to Vote. You would have to wait {years} more years!!")


#Age is less then 0 or more than 100
else:                               
    print("Please Enter a valid Age")
