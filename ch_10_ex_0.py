# Get the count of all words and display 5 most frequent words in a text

# Get txt file name from user and open txt file with file handle
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "clown.txt"
fhandle = open(fname, "r")

# Create empty dictionary to store words and their frequency
histogram = dict()

# Traverse through every line in the txt file
# Strip this line of unnecessary whitespaces

for line in fhandle:
    line = line.strip()
    # Split the line into a list of individual words based on space delimiter
    wds = line.split()
    # Traverse through the list of words from the line
    # Update count if word already in dictionary or create new key:value pair if not
    for w in wds:
        histogram[w] = histogram.get(w, 0) + 1

# print(histogram)

# Create empty list to store value:key pairs
# hist_list = list()

# Iterate through key:value pairs in the dictionary and add them as value:key to the list
# for k, v in histogram.items():
#     newt = (v, k)
#     hist_list.append(newt)

# print(hist_list)

# Sort the list of value:key in reverse order: from largest to smallest
# hist_list = sorted(hist_list, reverse=True)
# print(hist_list)

# Alternative condensed code for lines 26 up to 38
hist_list = sorted([(v, k) for k, v in histogram.items()], reverse=True)

# Print the 5 most common words, first k(key), then v(value)
for v, k in hist_list[:5]:
    print("{}: {}".format(k, v))
