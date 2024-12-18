#WAP to format a string (sentence)
#Enter your name and age

name=input("Enter your name: ")
age=int (input("Enter Your Age: "))

formatted_str= "My name is %s, and I am %d years old." % (name,age)
print(formatted_str)
