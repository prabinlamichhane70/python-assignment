# Write a Python function that takes a list of words and returns the length of the longest one.

def longest_word(list_of_word):
    words_len = []
    for n in list_of_word:
        words_len.append((len(n), n))
    words_len.sort()
    return words_len[-1][1]

print(longest_word(["hello", "binoculars", "Backend"]))