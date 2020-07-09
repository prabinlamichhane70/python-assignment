# Write a Python function that takes a number as a parameter and check the number is prime or not.
def test_prime_or_not(number):
    if (number == 1):
        return False
    elif (number == 2 ):
        return True
    else:
        for i in range(2, number):
            if (number % i == 1):
                return ("Prime number")
            else:
                return ("Composite number")
        return True
print (test_prime_or_not(14))