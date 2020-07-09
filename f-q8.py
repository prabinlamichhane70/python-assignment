# Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Sample List : [1,2,3,3,3,3,4,5], Unique List : [1, 2, 3, 4, 5]

def my_uni_list(myList):
    print ("Sample List is: ",myList)
    n = []
    for x in myList:
        if x not in n:
            n.append(x)
    return n
   
print(my_uni_list([1,2,3,3,3,3,4,5]))