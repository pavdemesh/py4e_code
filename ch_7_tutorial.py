fhand = open("mbox.txt", "r")
print(fhand)
counter = 0
for line in fhand:
    counter += 1
print(counter)
fhand.close()

print("-----------------")

xfile = open("mbox-short.txt", "r")
inp = xfile.read()
print(len(inp))
print(inp[:20])
xfile.close()

print("-----------------")

myfile = open("mbox-short.txt", "r")
for line in myfile:
    if line.startswith("From:"):
        print(line.rstrip())
myfile.close()

print("-----------------")

nfile = open("mbox-short.txt", "r")
for line in nfile:
    line = line.rstrip()
    if "@uct.ac.za" not in line:
        continue
    print(line)
nfile.close()

print("-----------------")

input_name = input("Enter file name: ")
try:
    rfile = open(input_name, "r")
except FileNotFoundError:
    print("Bad file name")
    exit()
lcounter = 0
for line in rfile:
    if "Subject:" in line:
        lcounter += 1
print("Number of line in", input_name, "is", lcounter)
nfile.close()

print("-----------------")
