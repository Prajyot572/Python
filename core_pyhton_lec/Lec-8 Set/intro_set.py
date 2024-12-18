'''
    A Set in Python programming is an unordred collection data type that is
iterable and has no dublicate elements. While sets are mutable meaning you
can add or remove elements after their creation.
'''

#Creation of Set
set_a={5,8,67,3}
print("The SET A is : ",set_a)

set_b={6,5,7,6}     #Set does not allow duplicate elements
print("The SET B is : ",set_b) 

set_c={7,9,78,4}
print("The SET C is : ",set_c)


#Set Union Operations
set_ab=set_a.union(set_b)
print(f"The union of set a and set b will be: {set_ab}   #No values are repeated")

#2 or more set union operations
set_abc=set_a.union(set_b,set_c)
print(f"The union of all the above set will be: {set_abc}")

#Using Union Operator " | "  to union
result=set_a|set_b|set_c
print(f"The union of all the above set will be: {result}")

#intersection method
abc=set_a.intersection(set_b)
print("The common element between set a and set b is: ",abc)

