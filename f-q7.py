# Write a Python function that accepts a string and calculate the number ofupper case letters and lower case letters.
# Sample String : 'The quick Brow Fox' Expected Output : No. of Upper case characters : 3 ,  No. of Lower case Characters : 12

def string_upp_low(name):
    upper_count = 0
    lower_count = 0
    for i in name:
        if i.isupper():
            upper_count = upper_count + 1
        elif i.islower():
            lower_count = lower_count + 1
        else:
            pass
    return "Number of Upper case letter is", upper_count ,"Number of Lower case letter is ", lower_count
# print (string_upp_low("Hello World"))
name = str(input("Enter a name: "))
print (string_upp_low(name))
    

    