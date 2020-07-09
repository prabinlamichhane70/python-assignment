# Write a Python program to multiplies all the items in a list.
total = 1
list_item = [5,9,7,8,15,25,6,3]
for n in range (0, len(list_item)):
    total = total * list_item[n]
print("All multiply result is: ", total)