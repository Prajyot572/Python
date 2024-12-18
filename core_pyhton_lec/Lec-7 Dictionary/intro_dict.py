''' A Dictionary is a built-in data structure in Python that allows you to
store a collection of key value pairs

Dictionary is mutable and it is unorderes '''

my_dict={
    "std_id":123,
    "std_name":"Prajyot",
    "course":"MCA"
}

print(my_dict)

x=my_dict["course"]
print("The course selected is",x)

x=my_dict.get("std_id")
print(x)


#Get all the keys from specified dictionary
y=my_dict.keys()
#print("The keys present are: ",y)

#To update dictionary element
my_dict.update({"std_name":"Rick"})
print(my_dict)

#To add new element in the dictionary
my_dict["fees"]=76000
print(my_dict)

my_dict["std_Addr"]="Uran"
print(my_dict)

#To remove certain element from the dictionary
my_dict.popitem()
print(my_dict)

#to get keys from the dictionary
for i in my_dict.keys():
    print(i)

for x,y in my_dict.items():
    print(x,y)


