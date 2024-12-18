#WAP to get factorial of a number using function.

#factorial function
def factorial(n):
    if n==0:
        return 1

    else:
        return n*factorial(n-1)

#input number
n=int(input("Enter a number: "))

#calling function
ans=factorial(n)
print(f"Factorial of the {n} number is {ans}")
    
