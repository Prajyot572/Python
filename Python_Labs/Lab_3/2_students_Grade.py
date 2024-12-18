'''WAP to create dictionaries for below task and perform all the above
operations on
a) Each student in a school is associated with their grade.'''

dict_students={
    "Prajyot":"A Grade",
    "Sameer":"A+ Grade",
    "Rahul":"C+ Grade",
    "Raj":"B Grade",
    "Ram":"O+ Grade"
    }
print("A)Creation of dictionary: ")
print(dict_students)

#check which key is associated to which value
x=dict_students["Prajyot"]
print("B) check which key is associated to which value: ")
print(f"The grades of Prajyot are {x}")

#to know the value of the key
x=dict_students.get("Ram")
print("C) to know the value of the key: ")
print(x)

#To update dictionary element
dict_students.update({"Prajyot":"O+ Grade"})
print("D) To update dictionary element: ")
print(dict_students)

#To add new element in the dictionary
dict_students["Ravi"]="A+ Grade"
print("E) To add new element in the dictionary: ")
print(dict_students)

#To remove certain element from the dictionary
dict_students.popitem()
print("F) To remove certain element from the dictionary: ")
print(dict_students)

#to get keys from the dictionary
print("G) to get keys from the dictionary: ")
for i in dict_students.keys():
    print(i)
#print dictionary in vertical line
print("H) Print dictionary in vertical line")
for x,y in dict_students.items():
    print(x,":",y)
