# Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7) Expected Output : 20
def my_simple_list(myNumbers):
    number = 0
    for i in myNumbers:
        number = number + i
    return number

print(my_simple_list([8, 2, 3, 0, 7]))
