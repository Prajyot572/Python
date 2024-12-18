'''WAP to create dictionaries for below task and perform all the above
operations on

a) Each customer ID in a company is associated with a customer.'''

dict_customer={
    "1":"Prajyot",
    "2":"Sameer",
    "3":"Rahul",
    "4":"Raj",
    "5":"Ram"
    }
print("A)Creation of dictionary: ")
print(dict_customer)

#check which key is associated to which value
x=dict_customer["1"]
print("B) check which key is associated to which value: ")
print(f"The customer whose ID 1 is: {x}")

#to know the value of the key
x=dict_customer.get("4")
print("C) to know the value of the key: ")
print(x)

#To update dictionary element
dict_customer.update({"1":"Ram"})
dict_customer.update({"5":"Prajyot"})
print("D) To update dictionary element: ")
print(dict_customer)

#To add new element in the dictionary
dict_customer["6"]="Ravi"
print("E) To add new element in the dictionary: ")
print(dict_customer)

#To remove certain element from the dictionary
dict_customer.popitem()
print("F) To remove certain element from the dictionary: ")
print(dict_customer)

#to get keys from the dictionary
print("G) to get keys from the dictionary: ")
for i in dict_customer.keys():
    print(i)
#print dictionary in vertical line
print("H) Print dictionary in vertical line")
for x,y in dict_customer.items():
    print(x,":",y)

