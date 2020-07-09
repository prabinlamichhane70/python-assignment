# Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
def lam_fun(n):
    return lambda a: a*n
result = lam_fun(2)
print("50 Multiply by 2 = ",result(50))
