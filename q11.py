# Write a Python program to count the occurrences of each word in a given sentence.
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum'))

