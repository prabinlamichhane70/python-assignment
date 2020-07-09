# Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7) Expected Output : -336

def my_list_to_multiply(myNumbers):
    numbers = 1
    for i in myNumbers:
        numbers = numbers * i
    return numbers
print (my_list_to_multiply([ 8, 2, 3, -1, 7]))
