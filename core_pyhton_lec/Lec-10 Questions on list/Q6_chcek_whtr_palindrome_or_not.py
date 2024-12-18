#Q.6) WAP to check whether the list is palindrome or not


list1=[1,2,3,4,5,6]

temp=list1
rev=0

for n in list1:
    (n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10

elif rev==temp:
    print("The Number is Palindrome")

else:
    print("The Number is not Palindorme")


    
