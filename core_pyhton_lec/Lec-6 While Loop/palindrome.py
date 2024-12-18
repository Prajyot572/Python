#WAP to chceck whether the number is palindrome or not
#n=434    rev=434 ==palindrome


n=int (input("Enter a number: "))
temp=n

rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print("The Order will be: ",rev)

if rev==temp:
    print("The Number is Palindrome")

else:
    print("The Number is not Palindorme")
