import re

hand = open('mbox-short.txt', "r")
for line in hand:
    line = line.rstrip()
    x = re.findall(r'[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    if len(x) > 0:
        print(x)
hand.close()

print("-----------------")

hand = open('mbox-short.txt', "r")
for line in hand:
    line = line.rstrip()
    x = re.findall(r'^X-.*: [0-9.]+', line)
    if len(x) > 0:
        print(x)
hand.close()

print("-----------------")

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall(r'^X\S*: ([0-9.]+)', line)
    if len(x) > 0:
        print(x)
hand.close()

print("-----------------")

# Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39772
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall(r'^Details:.+rev=([0-9.]+)', line)
    if len(x) > 0:
        print(x)
hand.close()
