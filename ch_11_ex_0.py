import re

# Create handle to open the file
fname = input("Enter file name:")
if len(fname) < 1:
    fname = "regex_sum_42.txt"
handle = open(fname, "r")

# Define variable to store the sum
res = 0

# Traverse trough the lines in the text
for line in handle:
    line = line.strip()
    # re.findall() will return a list of string with digits
    # map() casts type int on every item in the list
    # sum() adds those ints together
    res = res + sum(map(int, re.findall('[0-9]+', line)))
print(res)
