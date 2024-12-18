#WAP to reverse a given number for example n=123 rev=321

n=int (input("Enter a number: "))
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print("The Reverseble order of the given number is: ",rev)
    
