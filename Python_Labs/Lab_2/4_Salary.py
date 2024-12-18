#WAP to accept basic salary from user and Give 10% of DA on Basic Salary,
#12% HRA on basic salary to employee if the salary is more than 50000.
#Calculate the total salary

#Taking input as a salary
basic_salary=int (input("Enter your Salary: ₹"))

#10% DA
da=basic_salary*(10/100)

#Add 10% DA to basic salary
salary=basic_salary+da

#12% HRA on basic_salary
hra=basic_salary*(12/100)

#If basic salary is more than 50000
if basic_salary>=50000:
    total_salary=basic_salary+da+hra
    print(f"Your DA will be: ₹{da}")
    print(f"Your HRA will be: ₹{hra}")
    print(f"Yout total salary will be: ₹{total_salary}")

    
#If basic salary is less than 50000
else:
    print(f"Your DA will be: ₹{da}")
    print(f"Yout total salary will be: ₹{salary}")
