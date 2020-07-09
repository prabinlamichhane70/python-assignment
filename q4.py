#Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
#Sample String : 'abc', 'xyz' Expected Result : 'xyc abz'
def mix_char(a, b):
  new_x = b[:2] + a[2:]
  new_y = a[:2] + b[2:]

  return new_x + ' ' + new_y
print(mix_char('abc', 'xyz'))