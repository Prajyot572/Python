#Q4. Perform intersection operation on list

#creation  of list
List1=[1,2,3,4,5,6]
List2=[4,5,6,7,8,9,10]


#intersection of two list by converting them into set
intersection=list(set(List1) & set(List2))

#printitng the output
print("List after intersection of two list: ",intersection)

