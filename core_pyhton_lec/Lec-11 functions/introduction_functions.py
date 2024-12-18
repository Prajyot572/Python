#function is self contained block of  statement which has specific task to
#perform same block of code can be reused whenever required.

def myfunction():
    print("Hello all to the world of struggles")

myfunction()

def add(a,b):
    c=a+b
    print("The addition is",c)


a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

add(a,b)
