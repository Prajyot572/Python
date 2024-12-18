'''WAP to create dictionaries for below task and perform all the above
operations on
a) Each product in a supermarket is associated with its price.'''

#Creation of dictionary
dict_product={
    "Lays":"₹10",
    "Rice":"₹60/kg",
    "Wheat":"₹40/kg",
    "Milk":"₹36/ltr",
    "Paneer":"₹70/kg",
    }
print("A)Creation of dictionary: ")
print(dict_product)

#check which key is associated to which value
x=dict_product["Milk"]
print("B) check which key is associated to which value: ")
print(f"The prize of the Milk is {x}")

#to know the value of the key
x=dict_product.get("Lays")
print("C) to know the value of the key: ")
print(x)

#To update dictionary element
dict_product.update({"Lays":"₹20"})
print("D) To update dictionary element: ")
print(dict_product)

#To add new element in the dictionary
dict_product["Kesar"]="₹500/gms"
print("E) To add new element in the dictionary: ")
print(dict_product)

#To remove certain element from the dictionary
dict_product.popitem()
print("F) To remove certain element from the dictionary: ")
print(dict_product)

#to get keys from the dictionary
print("G) to get keys from the dictionary: ")
for i in dict_product.keys():
    print(i)
#print dictionary in vertical line
print("H) Print dictionary in vertical line")
for x,y in dict_product.items():
    print(x,":",y)
