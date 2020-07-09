# Write a Python script to merge two Python dictionaries.

dict1 = {'a':10, 'b':20}
dict2 = {'c':40, 'd':30}
dict = dict1.copy()
dict.update(dict2)
print(dict)