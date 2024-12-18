'''
Ordered:
When we say that tuples are ordered, it means that the items have defined
order, and that order will not change.

Unchangeable:
Tupple are unchangeable, meaning that we cannot change, add or remove items
after the tuple has been created.

Allow Duplicate":
Since tuples are indexed, they can have items with the same value:
'''

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)


#find the length of the tuple
print(len(thistuple))

#tuple is also recognized by its index no.
print(thistuple[0])
print(thistuple[4])

print(thistuple[2:4])
