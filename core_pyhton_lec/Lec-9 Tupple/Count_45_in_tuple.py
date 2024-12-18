#WAP to count the 45 in the tuple

tup2=(45,[34,89],80,73,45,45,90)

print("The 45 occurs",tup2.count(45),"times")

tup2[1][0]=45
print(tup2)

'''
tuple can not be changed
tup2[2]=78
print(tup2)
'''
