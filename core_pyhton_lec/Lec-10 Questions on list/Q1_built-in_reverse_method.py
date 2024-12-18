#Q.1) Write a function to reverse a list without using :
#the built-in reverse() method:

def rev_lst(l):
    return l[::-1]

l=[98,87,45,78]
print("The Given List: ",l)
print("The reverse of the given list is: ",rev_lst(l))
