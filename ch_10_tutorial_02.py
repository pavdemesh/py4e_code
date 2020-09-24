directory = dict()
print(directory)

first = 1
last = 2
number = 50098

directory[first, last] = number

directory["alpha"] = 48

print("keys:", list(directory.keys()))
print("values:", list(directory.values()))
print("-------------")

for key in directory:
    print(key, ":", directory[key])
