file_name = input("Enter file name: ")
fhand = open(file_name, "r")
counter = 0
for line in fhand:
    line.strip()
    line = line.split()
    if len(line) < 2:
        continue
    if line[0] == "From":
        print(line[1])
        counter += 1
print("There were %d lines in the file with From as the first word" % counter)
