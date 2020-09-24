import string
# Create file handle
fhand = open('romeo-full.txt', 'r')
# Create empty dictionary to store words (key) and their count (value)
counts = dict()

for line in fhand:
    # Remove all punctuation in the line
    line = line.translate(str.maketrans('', '', string.punctuation))
    # Make line lowercase
    line = line.lower()

    # Create a list with words from the line split based on space
    words = line.split()
    # For each word in the line: add to dictionary or increase count by 1
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# Sort the dictionary by value
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

# Sort the list by values in descending order
lst.sort(reverse=True)

for val, key in lst[:10]:
    print(key, ":", val)
