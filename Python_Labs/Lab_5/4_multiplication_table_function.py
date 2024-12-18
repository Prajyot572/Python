#WAP to get table of a number using function

#creating function for a multiplication table of any number
def multiplication(n):
    for i in range(1,11):
        print(f"{n}x{i}={n*i}")


#Input number
n=int(input("Enter any number you want multiplication number of: "))

#calling function
multiplication(n)
