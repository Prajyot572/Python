#WAP to calculate Simple Interest

#Enter your details
P=int (input("Enter valid Principle amount: ")) #P = Priciple Amount
N=int (input("Enter Number of Years: ")) #N = Number of Years
R= 8 #R = Rate of Intrest in %
print(f"Your Rate of Interest will be: {R} % ")

#Formula
Simple_Interest= P*R*N/100
print(f"The Simple Interest will be: ₹{Simple_Interest} ")
