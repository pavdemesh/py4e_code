# Write a program which repeatedly reads numbers until
# the user enters “done”. Once “done” is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than a number, detect their mistake using try and except and
# print an error message and skip to the next number.

total = 0
counter = 0
avg = 0
while True:
    user_input = input("Enter a number: ")
    if user_input == "done":
        # print("Total: {}, Count: {}, Average: {}".format(total, counter,  avg))
        break
    try:
        numeric_input = int(user_input)
    except ValueError:
        print("Bad input!")
        continue
    total += numeric_input
    counter += 1
    avg = total / counter

print("Total: {}, Count: {}, Average: {}".format(total, counter, avg))
