#WAP to get sum of digits present in a number.
#example: n=678 sum=21

n=int (input("Enter a number: "))

sum1=0
while(n>0):
    rem=n%10
    sum1=sum1+rem
    n=n//10
print("The Addition of the number will be: ",sum1)
