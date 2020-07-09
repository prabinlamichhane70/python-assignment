# Write a Python program to filter a list of integers using Lambda.
myList = [1,2,3,4,5,6,7,8,9]
print ("Non filter list : ",myList)
even_number_in_list = list(filter(lambda n: n%2 == 0, myList))
print ("Even number in list: ",even_number_in_list)
odd_number_in_list = list(filter(lambda n: n%2 == 1, myList))
print ("Odd number in list: ",odd_number_in_list)
