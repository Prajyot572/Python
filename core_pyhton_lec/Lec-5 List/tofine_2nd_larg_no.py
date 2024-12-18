#WAP to find second largest element

marks=[34,56,23,89,54]

for i in range(0,5):
    for j in range(i+1,5):
        if marks[j]>marks[i]:
            temp=marks[i] #saves the value at index i to temp.
            marks[i]=marks[j] #assigns the larger value (at index j) to the index i.
            marks[j]=temp #assigns the original value of marks[i] (now stored in temp) to index j.

print(marks)
print(marks[1])
