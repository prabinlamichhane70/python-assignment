# Write a Python program to remove duplicates from a list.
duplicate_list = [5, 7, 10, 34, 5, 2, 34, 5] 

def Remove(duplicate_list): 
    final_list = [] 
    for num in duplicate_list: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 
print(Remove(duplicate_list)) 