#Q1. WAP tpo create dynamic list where you will ask user to enter 5 elements
#in it and perform insert new element and delete on element operation on it.



#Making User input of 5 elements
list1=[]
for i in range(5):
    element=input(f"Enter element {i+1}: ")
    list1.append(element)
    print("Here is your list created: ",list1)



#Adding a new element in the list
list1.append(input("Enter a element to add: ")) #making a user input
print("Here is your updated list: ",list1)


#Deleting a Element from the list
list1.remove(input("Enter a element to delete: ")) #making a user input
print("Here is your updated list: ",list1)
