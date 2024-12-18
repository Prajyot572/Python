#Q.2) WAP to find second largest number in a list


list1=[89,67,54,65,89,78]

#converting list into set
remove_duplicate=(list(set(list1)))
print("The final list is: ",remove_duplicate)

sorted_list=sorted(remove_duplicate)
print("The sorted list is: ",sorted_list)

print("The second largest number is: ",sorted_list[-2])
            
