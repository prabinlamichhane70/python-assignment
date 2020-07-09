# Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9] Expected Result : [2, 4, 6, 8]
def check_even_number(numbers):
    myList = []
    for num in numbers:
        if num % 2 == 0:
           myList.append(num)
    return myList
print (check_even_number([1,2,3,4,5,6,7,8,9]))





