# Write a Python program to square and cube every number in a given list of integers using Lambda.
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list:", myList)
square_nums = list(map(lambda x: x ** 2, myList))
print("Square number from list", square_nums)
cube_nums = list(map(lambda x: x ** 3, myList))
print("Square number from list",cube_nums)