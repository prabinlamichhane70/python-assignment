# Write a Python program to sort a list of dictionaries using Lambda.
myDict = [{"name": "Ram", "age": 89},{'name': "hari", "age": 85},]
print ("Original Dictionary is ", myDict)
sortedDict = sorted(myDict, key = lambda x: x['age'])
print ("Sorted Dictionary is", sortedDict)
