# Write a Python script to check whether a given key already exists in a dictionary.
dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def key_present_or_not(x):
  if x in dict:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
key_present_or_not(5)
key_present_or_not(9)