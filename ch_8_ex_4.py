file_name = input("Enter file name: ")
fhand = open(file_name, "r")

words = list()

for line in fhand:
    tmp = line.split()
    for word in tmp:
        if word not in words:
            words.append(word)
words.sort()
print(words)
