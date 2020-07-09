# Write a Python program to sort a list of tuples using Lambda.
myTuple = [('a',85),('b',89),('c',87),('d',88),('e',75),('f',5),('g',3),('h',1),('i',15),('j',50)]
print ("Original Tuple is ", myTuple)
myTuple.sort(key = lambda x: x[1])
print ("Sorted tuple is", myTuple)
