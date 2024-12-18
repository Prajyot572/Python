t1=("Prajyot",80,"O Grade",56000,"Uran")
print(t1)

print(type(t1))

#slicing a tuple
print(t1[1:4])
print(t1[2:])
print(t1[:5]) #outer value is excluding


#find length of the tuple
print("The length of the tuple is: ",len(t1))

#you can also give negative indexing
print(t1[-2])
print(t1[-1])

#Note:
#1) List is a collection which is ordered and changeable.
#2) List Allows duplicate members.
#3) Tuple is a collection which is ordered and unchangeable.
#4) Tuple Allows duplicate members.

t2=list(t1)
print(t2)

t2[2]="A in sports"
print(t2)

for i in t2:
    print(i)
