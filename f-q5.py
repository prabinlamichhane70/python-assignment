# Write a Python function to calculate the factorial of a number (a non-negativeinteger). The function accepts the number as an argument.
def factorial_number(number):
    if number == 0:
        return 1
    else:
        return number*factorial_number(number-1)
number =  int(input("Enter a Positive Number "))
print (factorial_number(number))

