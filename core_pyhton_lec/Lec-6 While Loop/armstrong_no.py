#WAP to chechk whether the number is armstrong number or not 
#for example n=153 , 371
#sum= (3)*3*3+5*5*5+1*1*1
#   = 27+125+1=371

n=int (input("Enter a number: "))
sum1=0
while(n>0):
    rem=n%10
    sum1=sum1**3
    n=n//110
print("The amstrong will be: ",sum1)
