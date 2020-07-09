# Write a Python program to remove the nth index character from a nonempty string.
def remove_char(str, n):
      first_part = str[:n] 
      last_part = str[n+1:]
      return first_part + last_part
print(remove_char('world', 0))
print(remove_char('world', 2))
print(remove_char('world', 4))