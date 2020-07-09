# Write a Python function to find the Max of three numbers.
def max_of_three_number (a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

print(max_of_three_number(3,5,6))