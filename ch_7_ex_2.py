# Write a program that prompts for a file name, then opens that file and reads through the file,
# looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines
# and compute the average of those values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
# when you are testing below enter mbox-short.txt as the file name.

# Get file name from user
file_name = input("Enter file name: ")

# Handle for this file
fhand = open(file_name, "r")

# Set counter to 0 and total to 0
counter = 0
total = 0.0

# Traverse through lines in the file
for line in fhand:
    # Remove trailing spaces on both ends
    line = line.strip()
    # Check if the line contains required wording
    if line.startswith("X-DSPAM-Confidence:"):
        # If yes: increase counter by 1
        counter += 1
        # Extract the float point number: the number will start at the index where 0 is found
        # And up to the, that is why semicolon and no end index
        k = float(line[line.index("0"):])
        # Update total
        total += k
# Calculate and print out the result
result = total / counter
print("Average spam confidence: %.12f" % result)
