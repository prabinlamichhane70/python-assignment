#Write a Python program to count the number of characters (character frequency) in a string. Sample String : google.com'
#Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
test_str = "google.com"
all_freq = {} 
  
for i in test_str: 
    if i in all_freq: 
        all_freq[i] += 1
    else: 
        all_freq[i] = 1
  
# printing result  
print ("Count of all characters in GeeksforGeeks is :\n " +  str(all_freq)) 