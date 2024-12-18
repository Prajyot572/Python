#WAP to find maximum among two number

#funtion to find maximum among two numbers
def maximum(number1, number2):
    if number1>number2:
        print(number1,"is the maximum number among two numbers")

    else:
        print(number2,"is the maximum number among two numbers")

#input
number1=int(input("Enter 1st Number: "))
number2=int(input("Enter 2nd Number: "))

#calling function
maximum(number1, number2)
