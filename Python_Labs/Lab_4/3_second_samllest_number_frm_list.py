#Q3. WAP to find second smallest element in the list

#creation of list
List1=[4,8,3,2,1,7]

#arranging the list in Ascending order
duplicate_list=list(set(List1))
print(duplicate_list)


#2nd smallest number BY INDEXING
print("The second smallest number from the given list is: ",duplicate_list[1])
