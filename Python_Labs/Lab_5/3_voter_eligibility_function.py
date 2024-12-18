#WAP to chechk whether person can vote or not using function

#creating function
def vote(age):
    if (age>=18) and (age<=100):
        print("Yes you are eligible to vote")

    elif (age>0) and (age<18):
        n=18-age
        print(f"No you are not eligible to vote! you have to wait {n} more years")

    else:
        print("Please enter a valid Age")


#input age
age=int(input("Enter Your Age: "))

#calling function
vote(age)
